from Q08 import bola

bola01 = bola(cor="PRETO", circunferencia=35, material="Couro")

bola01.mostrarCor()
print("*"*15)
print("TROCANDO DE COR")
print("*"*15)
trocaCor = input("INFORME A COR DA BOLA: ")
bola01.trocarCor(trocadecor=trocaCor)