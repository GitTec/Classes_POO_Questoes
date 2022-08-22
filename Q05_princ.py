from Q05 import Papagaio

papagaio01 = Papagaio(nome="Zeus", idade=5)

for i in range(5):
    com=input("Informe a comida: ")
    papagaio01.oferecer(comida=com)
papagaio01.falar()
