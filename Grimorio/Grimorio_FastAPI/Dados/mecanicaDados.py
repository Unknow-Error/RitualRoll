import json
from Dados.dados import Dado

class TiradaMultiple:
    """
        Clase para instanciar tiradas de dados y realizar una tirada que requiera pasar un nivel de dificultad establecido para cada dado.
    """

    def __init__(self, dados = None, dificultad = None, bonus = 0, modo = True):
        self.dados = dados #Lista de dados
        self.dificultad = dificultad #Dificultad de la tirada
        self.bonus = bonus #Valor base que se suma a la tirada
        self.modo = modo #Modo de la tirada : Si hay que superar o no la dificultad
        self.valoresTirada = [] #Valores de los resultados de la tirada de cada dado
        self.valorNeto = 0 #Valor neto de la tirada
        self.valoresBooleanos = [] #Valores de exitos o fallas de cada dado (respecto a la dificultad a superar o al reves)
        self.resultadosCompleto = dict()
        self.resultadosCompletoJson = dict()

        if self.valoresTirada == []:
            self.tirar_dados()
            self.valor_neto()
            self.evaluar_exitos(self.modo)
            self.construir_resultado_completo()
            self.transformar_a_Json()

    def tirar_dados(self):
        """
            Tira los dados y devuelve una lista con los valores de cada dado.
        """
        valoresTirada = []

        for dado in self.dados:
            valoresTirada.append(dado.tirar())

        self.valoresTirada = valoresTirada

        return valoresTirada

    def valor_neto(self):
        """
            Calcula el valor neto de la tirada. Es la suma de todos los valores de los dados.
        """
        valor_neto = 0
        valor_neto += self.bonus

        if self.valoresTirada == []:
            self.tirar_dados()

        for valor in self.valoresTirada:
            valor_neto += valor

        self.valorNeto = valor_neto

        return valor_neto
        
    def evaluar_exitos(self, modo):
        """
            Evalua si la tirada de cada dado fue exitosa o no. Retorna un lista de booleanos.
            El modo es un booleano en el que True indica que el dado fue exitoso que indica si se debe superar la dificultad dada y False que indica si debe ser menor a la dificultad dada.
        """
        resultados_booleanos = [] 

        for valor in self.valoresTirada:
          if valor >= self.dificultad and modo:
            resultados_booleanos.append(True)
          else:
            resultados_booleanos.append(False)
        
        self.valoresBooleanos = resultados_booleanos

        return resultados_booleanos
    
    def construir_resultado_completo(self):
        """
            Todos los resultados en un diccionario.
        """

        resultadosTiradas = {}
        resultadosTiradas["dados"] = [{"caras": dado.caras, "valores": dado.valores} for dado in self.dados] # Porque los objetos Dados no son JSON serializables.
        resultadosTiradas["dificultad"] = self.dificultad
        resultadosTiradas["bonus"] = self.bonus
        resultadosTiradas["modo"] = self.modo
        resultadosTiradas["valores"] = self.valoresTirada
        resultadosTiradas["valorNeto"] = self.valorNeto
        resultadosTiradas["valoresBooleanos"] = self.valoresBooleanos
        
        self.resultadosCompleto = resultadosTiradas
      
        return resultadosTiradas
    
    def transformar_a_Json(self):
        """
            Formato de todos los resultados en JSON.
        """
        
        resultadosComplejosJson = json.dump(self.resultadosCompleto)
        self.resultadosCompletoJson = resultadosComplejosJson
        
        return resultadosComplejosJson
    
    def __str__(self):
        stringSalida = ""
        if self.bonus == 0:
            stringSalida += f"El resultado de la tirada {len(self.dados)}D{self.dados[0].caras} fue de un total de {self.valorNeto}"
        else:
            stringSalida += f"El resultado de la tirada {len(self.dados)}D{self.dados[0].caras}+{self.bonus} fue de un total de {self.valorNeto}"
        
        return stringSalida

    def __repr__(self):
        return f"TiradaMultiple({self.dados}, {self.dificultad}, {self.bonus}, {self.modo})"
    
class Tirada_CWoD_20(TiradaMultiple):
    """
        Clase para tiradas del sistema Classic World of Darkness 20th: tiene pifias, éxitos múltiples, especialización.
        Reglas:
        -Tiradas de 1D10 : Cantidad de dados segun nodos de Atributo + Habilidad
        -Dificultad : Establece el valor a superar por el dado
        -Regla del 10 : Si un dado sale con un 10, se lo cuenta como éxito y se vuelve a tirar, y si vuelve a salir 10 se repite acumulando más éxitos superados
        -Éxito: Cualquier dado que saque un número igual o superior a la dificultad.
        -Éxito crítico: Si salen varios 10s (2 o más) en los dados, puede haber éxito excepcional : Un éxito con efectos adicionales
        -Falla: Cualquier dado que saque un número inferior a la dificultad.
        -Pifia (Falla crítica): Dado con 1. Si no hay éxitos (o muy pocos) y salen 1 o más 1s en los dados, se considera fracaso castastrófico.
    """
    def __init__(self, dados = None, dificultad = 6):
        super().__init__(dados, dificultad, 0, True)
        self.resultadoTirada = dict() # Se almacena el numero de exitos, exitos criticos, "regla del 10" y pifias
        self.resultadoTiradaJson = dict()

        if self.resultadoTirada == {}:
            self.tirar_dados()
            self.evaluar_exitos()
            self.transformar_a_Json()

    def tirada_regla_del_diez(self):
        """
            Tira los dados y devuelve una lista con los valores de cada dado.
        """
      
        valores_regla_del_diez = []

        for valor in self.valoresTirada:
            if valor == 10:
                valores_regla_del_diez.append(self.dados[0].tirar())

        self.valoresTirada += valores_regla_del_diez
        
        return valores_regla_del_diez

    def evaluar_exitos(self, modo=True):
        """
            Override del método de la clase padre siguiendo las reglas del sistema.
        """
        resultados_tiradas = dict()
        pifias = 0
        exitos = 0
        fallas = 0
        exitosCriticos = 0
        exitos_diez = 0

        for valor in self.valoresTirada:
            if valor >= self.dificultad:
                exitos += 1
            else:
                fallas += 1
            if valor == 10:
                exitos_diez += 1
            if exitos_diez >= 2 and valor == 10:
                exitosCriticos += 1
            if valor == 1:
                pifias += 1

        falloCritico = (fallas > exitos and pifias > 0)

        resultados_tiradas["valores"] = self.valoresTirada
        resultados_tiradas["exitos"] = exitos
        resultados_tiradas["fallas"] = fallas
        resultados_tiradas["exitosCriticos"] = exitosCriticos
        resultados_tiradas["pifias"] = pifias
        resultados_tiradas["falloCritico"] = falloCritico

        self.resultadoTirada = resultados_tiradas

        return resultados_tiradas
    
    def transformar_a_Json(self):
        """
            Transforma el resultado de la tirada a un formato JSON.
        """

        resultadoTiradaJson = json.dumps(self.resultadoTirada)
        self.resultadoTiradaJson = resultadoTiradaJson
      
        return resultadoTiradaJson

    def __str__(self):
        stringSalida = f"El resultado de la tirada {len(self.dados)}D{self.dados[0].caras}"
        for llave, valor in self.resultadoTirada.items():
            if llave == "valores":
                stringSalida += f" dio {valor}"
            if llave == "exitos":
                stringSalida += f" con {valor} exitos"
            if llave == "fallas":
                stringSalida += f" y {valor} fallas"
            if llave == "exitosCriticos" and valor > 0:
                stringSalida += f" con {valor} exitos criticos"
            if llave == "falloCritico" and valor == True:
                stringSalida += f" siendo un Fallo Catastrófico"

        return stringSalida

    def __repr__(self):
        return f"TiradaCWoD_20({self.dados}, {self.dificultad}, {self.bonus})"