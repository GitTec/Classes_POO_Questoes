from Q13_Imovel import Imovel
from Q13_Casa import Casa
from Q13_Predio import Predio


imovel1 = Casa(valor="10000", cor="vermelha", localizacao="Rua dos Princes", qtcomodos=5)
imovel1.casComodos()
imovel1.exibirDetalhes()

imovel2 = Predio(valor="10000", cor="vermelha", localizacao="Rua dos Princes", qtdAndares=15)
imovel2.qtdAndares()
imovel1.exibirDetalhes()
