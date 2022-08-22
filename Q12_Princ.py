from Q12_Pessoa import Pessoa
from Q12_PessoaFisica import PessoaFisica
from Q12_PessoaJuridica import PessoaJuridica

nompessoa = input("Informe seu nome: ")
tel = "88 9 9451-6587"
pessoa01 = Pessoa(nome=nompessoa, telefone=tel)

print("-"*30)
pessoa01.exibirNome()
print("*"*30)
pessoa01.exibirCartaoVisita()
print("*"*30)

pessoa02 = PessoaFisica(nome=nompessoa, telefone=tel, cpf="045.458.142-54", sexo="M", dtNascimento="05.02.1998")
pessoa02.procurarTrabalho()
print("*"*30)
pessoa03 = PessoaJuridica(nome=nompessoa, telefone=tel, cnpj="27.154.3265.142-25", dtFuncacao="2005")
pessoa03.contratar()
