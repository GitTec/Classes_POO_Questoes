from datetime import datetime
import math

class Animais:
    def __init__(self, nome, dtNasc, altura, corOlhos):
        self.__nome = nome
        self.__dtNasc = dtNasc
        self.__altura = altura
        self.__corOlhos = corOlhos

#Caso eu queira printar um print
    def __str__(self):
        return print(f"Um {self.__nome} tem-> DT Nasc.{self.__dtNasc} olhos: {self.__corOlhos} e altura {self.__altura}")

    def andar(self, passos):
        print(f"Está andando {passos}")

    def get_nome(self):
        return self.__nome

    def comer(self):
        print(f"O {self.__nome} está comendo")

    def calcularIdade(self):
        anoAtual = datetime.now()
        qtdDias = (anoAtual - self.__dtNasc).days
        idade = math.floor(qtdDias / 365)
        return idade
