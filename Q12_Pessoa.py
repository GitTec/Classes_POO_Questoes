
class Pessoa:

    def __init__(self, nome, telefone):
        self.__nome = nome
        self.__telefone = telefone

    def exibirNome(self):
        print(f"Meu nome é josé {self.__nome}")

    def exibirCartaoVisita(self):
        print(f"Ola, Seja bem vindo {self.__nome}")

    def get_nome(self):
        return self.__nome