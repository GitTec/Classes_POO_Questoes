class Pessoa:
    nome = ""
    idade = 0
    sexo = "M"

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

    def mensagem(self, msg):
        print(f"Olá meu nome é {self.nome} e {msg}")
