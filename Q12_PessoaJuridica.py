from Q12_Pessoa import Pessoa


class PessoaJuridica(Pessoa):

    def __init__(self, nome, telefone, cnpj, dtFuncacao):
        super().__init__(nome, telefone)
        self.cnpj = cnpj
        self.dtFundacao = dtFuncacao

    def contratar(self):
        print(f"{self.get_nome()} você está contratado")
