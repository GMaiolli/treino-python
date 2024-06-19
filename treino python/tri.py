#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#a soma de dois lados é sempre menor que o terceiro lado.

a = float(input("Digite o valor da reta 1: "))
b = float(input("Digite o valor da reta 2: "))
c = float(input("Digite o valor da reta 3: "))

if b - c < a < b + c and a - c < b < a + c and b - a < c < b + a:
    print("eh um triangulo")
else:
    print("nao eh um triangulo")