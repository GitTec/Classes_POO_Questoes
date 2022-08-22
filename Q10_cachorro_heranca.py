from Q10_animais_heranca import Animais


class Cachorro(Animais):
    #Aqui passo tudo
    def __init__(self, raca, nome, dtNasc, altura, corOlhos):
        #Aqui só o que herdo
        super().__init__(dtNasc=dtNasc, nome=nome, altura=altura, corOlhos=corOlhos)
        self.__raca = raca

    def __str__(self):
        idade = super().calcularIdade()
        return f"Um {super().get_nome()} com {idade} anos de idade"

    def latir(self):
        print(f"O {super().get_nome()} está latindo")

