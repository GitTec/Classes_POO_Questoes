class Cachorro:
    nome_animal = ""
    cor = ""
    idade = 0
    raca = ""

    def __init__(self, nome_animal, cor, idade, raca):
        self.nome_animal = nome_animal
        self.cor = cor
        self.idade = idade
        self.raca = raca

    def nomeando (self):
        print(f"O NOME DO MEU CACHORRO É {self.nome_animal}")