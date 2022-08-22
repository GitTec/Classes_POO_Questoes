from Q01 import Questao01

val1 = int(input("INFORME 1° VALOR: "))
val2 = int(input("INFORME 2° VALOR: "))
val3 = int(input("INFORME 3° VALOR: "))

q01 = Questao01(val1=val1, val2=val2, val3=val3)

#Preciso criar a variavel aqui para receber o valor que foi retornado
calcMedia = q01.calcularMedia(val1, val2, val3)
#Aqui passo a variavel
q01.verificarAprovacao(calcMedia)