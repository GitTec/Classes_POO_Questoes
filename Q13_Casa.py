from Q13_Imovel import Imovel


class Casa(Imovel):
    def __init__(self, valor, cor, localizacao, qtcomodos):
        super().__init__(valor=valor, cor=cor, localicao=localizacao)
        self.qtcomodos = qtcomodos

    def casComodos(self):
        print("*"*30)
        print(f"UMA CASA COM 6 COMODOS")
