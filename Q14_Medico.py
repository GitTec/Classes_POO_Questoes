from Q14_Funcionario import Funcionario


class Medico(Funcionario):
    def __init__(self, nome, idade, salario, especializacao):
        super().__init__(nome=nome, idade=idade, salario=salario)
        self.__especializacao = especializacao

    def trabalhar(self):
        print("-" * 15)
        super().trabalhar()
        print("Estou muito ocupado")
        print("-" * 15)