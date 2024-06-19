altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

num = int(input("Teste: "))

metro_quad = altura * largura

print("A quantidade de litros nessesarios eh de {:.3f}".format(metro_quad / 2))

print("Seu antecessor {} e seu sucessor {}".format(num - 1, num + 1))