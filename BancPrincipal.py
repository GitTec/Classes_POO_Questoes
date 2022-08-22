from ContaBancaria import ContaBancaria

nome = input("Digite o seu nome")
codigo = input("Digite o codigo da conta")

conta1 = ContaBancaria(codigoConta=codigo,nmTitular=nome, banco="BB")

conta1.exibirConta()
conta1.depositar(100)
conta1.depositar(200)
conta1.depositar(600)
conta1.depositar(900)
conta1.alterarTitular()
print(f"o titular da conta é {conta1.get_titular()}")
#conta1.nmtitular = "Estudando"
conta1.set_titular("EstudandoPOO")
print(f"O banco é {conta1.banco}")