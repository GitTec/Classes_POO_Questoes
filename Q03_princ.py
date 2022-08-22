from Q03 import Cachorro
nomCachorro = input("informe o nome do cachorro: ")
corCachorro = input("informe a cor do cachorro: ")
id = int(input("Informe a idade: "))
raca = input("Informe a raca: ")

cachorro01 = Cachorro(nome_animal="do", cor="Preto", idade=6, raca="Pincher")
cachorro02 = Cachorro(nome_animal="re", cor="Branco", idade=5, raca="Poodle")
cachorro03 = Cachorro(nome_animal="me", cor="Verde", idade=4, raca="Boodogue")
cachorro04 = Cachorro(nome_animal="fa", cor="Cinza", idade=8, raca="Pastor Alemão")

cachorroespecial = Cachorro(nome_animal=nomCachorro, cor=corCachorro, idade=id, raca=raca)
cachorroespecial.nomeando()
