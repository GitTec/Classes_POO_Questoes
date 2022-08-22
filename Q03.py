class Cachorro:

    def __init__(self, nome_animal, cor, idade, raca):
        self.nome_animal = nome_animal
        self.cor = cor
        self.idade = idade
        self.raca = raca

    def nomeando (self):
        print(f"O NOME DO MEU CACHORRO É {self.nome_animal}")
        print(f"Meu cachorro tem {self.idade}")