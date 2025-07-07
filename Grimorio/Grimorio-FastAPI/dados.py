import random

class Dado:
    """
        Clase Base para instanciar dados de diferentes caras y valores.
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
    
