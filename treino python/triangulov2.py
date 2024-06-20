#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes


a = float(input("Digite o valor da reta 1: "))
b = float(input("Digite o valor da reta 2: "))
c = float(input("Digite o valor da reta 3: "))

if b - c < a < b + c and a - c < b < a + c and b - a < c < b + a:
    if a == b == c:
        print("As retas {} {} {} formam um triangulo equilátero!".format(a, b, c))
    elif a == b or a == c or b ==c:
        print("As retas {} {} {} formam um triangulo isósceles!".format(a, b, c))
    else:
        print("As retas {} {} {} formam um triangulo escaleno".format(a, b, c))
else:
    print("nao eh um triangulo")

#teste