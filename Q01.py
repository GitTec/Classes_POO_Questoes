class Questao01:

    def __init__(self, val1, val2, val3):
        self.val1 = val1
        self.val2 = val2
        self.val3 = val3


    def calcularMedia(self, v1, v2, v3):
        media = (v1 + v2 + v3) / 3
        print("-" * 50)
        print(f"A MÉDIA ENTRE AS NOTAS É {media:.2f}")
        print("-" * 50)
        return media

    def verificarAprovacao(self, media):
        if media >= 7:
            print("ALUNO APROVADO")
        else:
            print("ALUNO REPROVADO")
