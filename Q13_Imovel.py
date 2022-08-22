
class Imovel:

    def __init__(self, valor, cor, localicao):
        self.valor = valor
        self.cor = cor
        self.local = localicao

    def exibirDetalhes(self):
        print("COR VERMELHA")
        print("VALOR DE 10.000R$")
        print("LOCALIZADA NA RUA SEM FIM")
        print("*" * 30)