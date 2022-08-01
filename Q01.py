class Questao01:
    val1 = int(input("INFORME PRIMEIRO VALOR: "))
    val2 = int(input("INFORME SEGUNDO VALOR: "))
    val3 = int(input("INFORME TERCEIRO VALOR: "))
    media = int((val1 + val2 + val3)/3)


    def __init__(self, val1, val2, val3):
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3


    def calcularMedia (self, v1, v2, v3):
        print("-"*50)
        print(f"A MÉDIA ENTRE AS NOTAS É {v1, v2, v3}")
        print("-" * 50)


    def verificarAprovacao (media):
        if media >= 7:
            print("ALUNO APROVADO")
        else:
            print("ALUNO REPROVADO")


    #calcularMedia(val1, val2, val3)
    #verificarAprovacao(media)

