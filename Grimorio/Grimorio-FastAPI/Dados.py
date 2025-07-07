import random

class Dado:
    """
        Clase para instanciar dados de diferentes caras y valores.
    """
    def __init__(self, caras = None, valores = None):
        self.caras = caras #Numero de caras
        self.valores = valores #Lista de Valores
        if self.caras is not None:
            self.definir_valores()

    def definir_valores(self):
        """
        Define los valores numéricos del dado.
        """
        self.valores = []
        
        for i in range(self.caras):
            self.valores.append(i+1)

    def tirar(self):
        """
        Tira el dado y devuelve un valor aleatorio.
        """
        return random.choice(self.valores)

    def __str__(self):
        return f"Dado con {self.caras} caras y valores {self.valores}"
    
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
        
        for dado in self.dados:
          if dado.tirar() >= self.dificultad and modo:
            resultados_booleanos.append(True)
          else:
            resultados_booleanos.append(False)
        
        self.valoresBooleanos = resultados_booleanos

        return resultados_booleanos
