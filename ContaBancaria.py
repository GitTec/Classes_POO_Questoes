class ContaBancaria:

    def __init__(self, nmTitular, codigoConta, banco):
        self.__nmTitular = nmTitular
        self.__codigoConta = codigoConta
        self.__saldo = 0
        self.banco = banco

    def exibirConta(self):
        print(f"O nome do titular é {self.__nmTitular}")
        print(f"O numero da conta é {self.__codigoConta}")
        print(f"O saldo é {self.__saldo}")

    def depositar(self, valor):
        print(f"SALVANDO SALDO NO BANCO DE DADOS")
        print(f"voce depositou {valor}")
        self.__saldo += valor
        print(f"Seu novo saldo é de {self.__saldo}")

    def __alterarTitular(self,novoTitular):
        if novoTitular != "":
            self.__nmTitular = novoTitular
        else:
            print("nome invalido!!")
        print(f"Anexar assinatura")
        print(f"Alterado")
        self.__nmTitular=novoTitular

    def get_titular(self):
        return self.__nmTitular

    def set_titular(self, novoNome):
        self.__alterarTitular(novoNome)
