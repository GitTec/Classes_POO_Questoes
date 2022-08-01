class CC:
    numConta=""
    nmCorrent=""
    saldo=0

    def __init__(self, numConta, nmCorrent, saldo):
        self.numConta = numConta
        self.nmCorrent = nmCorrent
        self.saldo = saldo

    def alterarNome(self, novoNome):
        print("Meu novo nome é: ")
        self.nmCorrent = novoNome


    def deposito(self, valDep):
        #input("Qual valor deseja depositar? ")
        if valDep == 0:
            print("Você não tem o que depositar")
        else:
            self.saldo = valDep
            print(f"MEU NOVO SALDO É: {self.saldo}")

    def saque(self, valSaque):
        if valSaque > self.saldo:
            print("VOCÊ NÃO TEM ESSE SALDO")
        else:
            self.saldo = self.saldo - valSaque
            print(f"Valor após saque ficou de {self.saldo}R$")