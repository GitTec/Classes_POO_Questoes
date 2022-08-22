from Q06 import Papagaio
print("-" * 30)
nome = input("Informe o nome do Papagaio? ")
idade = int(input(f"Informe a idade {nome}: "))
print("-" * 30)

papagaio01 = Papagaio(nome=nome, idade=idade)
for i in range(3):
    comOferecida = input(f"Qual a {i + 1}° comida que pode me oferecer? ")
    papagaio01.oferecer(comida=comOferecida)

papagaio01.falar()
