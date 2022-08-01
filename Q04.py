class Gato:
    nome=""
    cor=""

    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def falar(self):
        print("MIAU MIAU")

    def comer(self):
        print(f"O GATO ESTÁ COMENDO")