import dados

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

        if self.valoresTirada == []:
            self.tirar_dados()
            self.valor_neto()
            self.evaluar_exitos(self.modo)


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
    
class TiradaCWoD_20(TiradaMultiple):
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
    def __init__(self, dados = None, dificultad = 6, bonus = 0, reglaDelDiez = True):
        super().__init__(dados, dificultad, bonus, True)
        self.resultadoTirada = dict() # Se almacena el numero de exitos, exitos criticos, "regla del 10" y pifias
        self.reglaDelDiez = reglaDelDiez # Si se aplica o no la regla del 10

        if self.resultadoTirada == {}:
            self.tirar_dados()
            self.evaluar_exitos()

    def tirar_dados(self):
      """
        Override del método de la clase padre siguiendo las reglas del sistema.
      """
      valoresTirada = []

      for dado in self.dados:
        valoresTirada.append(dado.tirar())
        if self.reglaDelDiez and valoresTirada[-1] == 10:
          while valoresTirada[-1] == 10:
            valoresTirada.append(dado.tirar())

      self.valoresTirada = valoresTirada

      return valoresTirada

    def evaluar_exitos(self):
      """
        Override del método de la clase padre siguiendo las reglas del sistema.
      """
      resultados_tiradas = dict() 
      pifias = 0
      exitos = 0
      exitosCriticos = 0

      for valor in self.valoresTirada:
        if valor == 1:
          pifias += 1
          resultados_tiradas["pifias"] = pifias
        elif valor >= self.dificultad:
          exitos += 1
          resultados_tiradas["exitos"] = exitos
        elif valor == 10:
          exitosCriticos += 1
          resultados_tiradas["exitosCriticos"] = exitosCriticos

      self.resultadoTirada = resultados_tiradas

      return resultados_tiradas  