from Q14_Funcionario import Funcionario
from Q14_Medico import Medico
from Q14_Programador import Programador

prog1 = Programador(nome="Jefferson", idade=24, salario=8500, linguagem="Python")
medico1 = Medico(nome="Jefferson", idade=24, salario=7000, especializacao="Medicina")

prog1.trabalhar()
medico1.trabalhar()

