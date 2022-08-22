from Q10_animais_heranca import Animais
from Q10_gato_heranca import Gato
from Q10_cachorro_heranca import Cachorro
from datetime import datetime

nome = "xano"
dtNasc = datetime(year=2010,month=5, day=4)
corOlho = "Verde"
altura = 0.60

gato01 = Gato(nome=nome, dtNasc=dtNasc, corOlhos=corOlho, altura=altura)
gato01.calcularIdade()
gato01.miar()
gato01.comer()
print(gato01)

nome = "dogao"
dtNasc = datetime(year=2010,month=6, day=5)
corOlho = "Preto"
altura = 1
raca = "pincher"

cachorro01 = Cachorro(nome=nome, dtNasc=dtNasc, corOlhos=corOlho, altura=altura, raca=raca)
cachorro01.calcularIdade()
cachorro01.latir()
cachorro01.comer()