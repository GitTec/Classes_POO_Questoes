from Q09 import CC

cc01 = CC(numConta="15252-4", nmCorrent="Gelson", saldo=0)


cc01.alterarNome("Silvio")
print(cc01.nmCorrent)
cc01.deposito(valDep=500)
cc01.saque(valSaque=250)