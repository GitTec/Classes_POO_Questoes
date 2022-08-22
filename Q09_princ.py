from Q09 import CC

numeroConta=input("INFORME O NUMERO DA CONTA: ")
nomeConta=input("INFORME O NOME DA CONTA: ")

cc01 = CC(numConta=numeroConta, nmCorrent=nomeConta, saldo=0)

print("*"*35)
print(f"SUA CONTA É: {cc01.numConta}")
print(f"PROPRITARIO DA CONTA: {cc01.nmCorrent}")
print("*"*35)

novoNome=input("QUAL O NOVO NOME DA CONTA: ")
#pedir pra usuario digitar o nome e numero da conta, criar a conta com esses valores informados
#depois eu peço o novo nome e alterar o nome, ai depois peço quanto quer sacar e depositar

cc01.alterarNome(novoNome)
print(cc01.nmCorrent)

#colocar esses em while true, e perguntar oq  pessoa deseja fazer, se 1-deposito e 2-saque, qual valor deseja sacar ou depositar
cc01.deposito(valDep=500)
cc01.saque(valSaque=250)