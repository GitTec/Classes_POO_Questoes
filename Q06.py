class Papagaio:
    print("-"*30)
    nome = input("Informe o nome do Papagaio? ")
    idade = int(input(f"Informe a idade {nome}: "))
    print("-" * 30)

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"Meu nome é {self.nome} e estou lascado de fome")

    def oferecer(self, comida):
        for i in range(3):
            comida = input(f"Qual a {i+1}° comida que pode me oferecer? ")

            if comida[i] == "cha" or comida[i] == "biscoito" or comida[i]=="cafe":
                print(f"O Papagaio {self.nome} está comendo {comida}")
            else:
                print(f"Não gosto de {comida}")