class bola:
    cor = ""
    circunferencia = 0
    material = ""

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circun = circunferencia
        self.material = material


    def trocarCor(self):
        trocaCor = input("INFORME A COR DA BOLA: ")
        self.cor = trocaCor
        print(f"A NOVA COR É: {trocaCor}")


    def mostrarCor(self):
        print(f"A COR DA BOLA É: {self.cor}")



