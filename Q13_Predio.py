from Q13_Imovel import Imovel


class Predio(Imovel):
    def __init__(self, valor, cor, localizacao, qtdAndares):
        super().__init__(valor=valor, cor=cor, localicao=localizacao)
        self.qtdAnd = qtdAndares

    def qtdAndares(self):
        print("*"*30)
        print("UM PRÉDIO COM 25 ANDARES")
