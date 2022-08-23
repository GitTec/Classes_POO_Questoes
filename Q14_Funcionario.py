
class Funcionario:

    def __init__(self, nome, idade, salario):
        self.__nome = nome
        self.__idade = idade
        self.__salario = salario

    def irParaReuniao(self):
        print("Estou indo para reuniao")

    def trabalhar(self):
        print("Estou trabalhando")
