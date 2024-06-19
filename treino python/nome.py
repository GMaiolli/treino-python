nome = input("Digite seu Nome: \n")

print("seu nome em caixa alta: \n{}".format(nome.upper()))
print("seu nome em minusculo: \n{}".format(nome.lower()))
nome2 = nome.split()
print("quantidade de letras do seu nome completo: \n{}".format(len(''.join(nome2))))
print("quantidade de letras no seu primeiro nome: \n{}".format(len(nome2[0])))