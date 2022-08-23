from Q14_Funcionario import Funcionario


class Programador(Funcionario):
    def __init__(self, nome, idade, salario, linguagem):
        super().__init__(nome=nome, idade=idade, salario=salario)
        self.__linguagem = linguagem

    def trabalhar(self):
        print("-"*15)
        super().trabalhar()
        print("Estou Codando")
        print("-"*15)