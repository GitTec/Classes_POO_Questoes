from Q11_Automovel import Automovel
from Q11_Carro import Carro
from Q11_moto import Moto

modelo = "Camaro Amarelo"
cor = "Vermelho"
placa = "FG450"

carro01 = Carro(modelo=modelo, cor=cor, placa=placa)
carro01.abastecer()

modelo = "Bros"
cor = "Preto"
placa = "TR250"
Moto01 = Moto(modelo=modelo, cor=cor, placa=placa)
Moto01.abastecer()