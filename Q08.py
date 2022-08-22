class bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circun = circunferencia
        self.material = material


    def trocarCor(self, trocadecor):
        self.cor = trocadecor
        print(f"A NOVA COR É: {trocadecor}")


    def mostrarCor(self):
        print(f"A COR DA BOLA É: {self.cor}")



