import random


class Robo:
    nome = ""
    vida = 100

    def __init__(self, nome):
        self.nome = nome

    def atacaRobo(self):
        sorteio = random.randint(10, 150)
        print("X-X"*9)
        print(f"    VIDA INICIAL {100}%")
        print(f"    SOFREU {sorteio}% DE DANO")
        print("X-X" * 9)
        calcVida=(self.vida - sorteio)

        if calcVida > 0:
            print(f"{self.nome} AINDA ESTA VIVO COM {calcVida}% DE VIDA")
        else:
            print(f"{self.nome} INFELIZMENTE BATEU O MOTOR")


