#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
while True:
    try:
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))


        if num1 > num2:
            print("O primeiro valor é maior")
            break
        elif num2 > num1:
            print("O segundo valor é maior")
            break
        else:
            print("Não existe valor maior, os dois são iguais")
            break
    except ValueError:
        print("Digite numeros validos!")