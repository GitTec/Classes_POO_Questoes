
class Automovel:

    def __init__(self, modelo, cor, placa):
        self.modelo = modelo
        self.cor = cor
        self.placa = placa
        self.cap_tanque = 60
        self.comb_tanque = 0

    def abastecer(self):
        if self.comb_tanque == 0:
            print("Abastencendo o automovel")
        elif self.comb_tanque < self.cap_tanque:
            print("Ainda da pra abastecer")
        elif self.comb_tanque == self.cap_tanque:
            print("O tanque ta cheio")
        else:
            print("Imvalido")