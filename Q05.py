class Papagaio:
    nome = ""
    idade = 0

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"OI MEU NOME É {self.nome}")

    def oferecer(self, comida):
        if comida == "cha" or comida== "biscoito" or comida=="cafe":
            print(f"O Papagaio {self.nome} está comendo {comida}")
        else:
            print(f"Não gosto de {comida}")