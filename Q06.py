class Papagaio:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Meu nome é {self.nome} e estou lascado de fome")

    def oferecer(self, comida):
            if comida == "cha" or comida == "biscoito" or comida =="cafe":
                print(f"O Papagaio {self.nome} está comendo {comida}")
            else:
                print(f"Não gosto de {comida}")