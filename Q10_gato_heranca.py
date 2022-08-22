from Q10_animais_heranca import Animais


class Gato(Animais):
    def __init__(self, nome, dtNasc, altura, corOlhos):
        super().__init__(nome=nome, dtNasc=dtNasc, altura=altura, corOlhos=corOlhos)

    def __str__(self):
        idade = super().calcularIdade()
        return f"Um gato com {idade} anos de idade"

    def miar(self):
        print(f"O gato está miando")

