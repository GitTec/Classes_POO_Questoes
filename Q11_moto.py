from Q11_Automovel import Automovel


class Moto(Automovel):

    def __init__(self, modelo, cor, placa):
        super().__init__(modelo=modelo, cor=cor, placa=placa)


