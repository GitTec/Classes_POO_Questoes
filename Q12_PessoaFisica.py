from Q12_Pessoa import Pessoa


class PessoaFisica(Pessoa):

    def __init__(self, nome, telefone, cpf, sexo, dtNascimento):
        super().__init__(nome=nome, telefone=telefone)
        self.__cpf = cpf
        self.__sexo = sexo
        self.__dtNascimento = dtNascimento

    def procurarTrabalho(self):
        print(f"{super().get_nome()} esta procurando trabalho?")