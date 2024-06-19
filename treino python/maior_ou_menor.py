#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = int(input("Digite o primeiro numero:"))
num2 = int(input("Digite o segundo numero:"))
num3 = int(input("Digite o terceiro numero:"))

if num1 > num2 and num1 > num3:
    nummaior = num1
elif num2 > num1 and num2 >num3:
    nummaior = num2
else:
    nummaior = num3

if num1 < num2 and num1 < num3:
    nummenor = num1
elif num2 < num1 and num2 < num3:
    nummenor = num2
else:
    nummenor = num3

print("{} eh o maior numero e {} eh o menor numero!".format(nummaior, nummenor))