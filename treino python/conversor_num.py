#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um numero inteiro: "))
while True:
    print('''Escolha uma das bases para conversão:
    [ 1 ] para binario
    [ 2 ] para octal
    [ 3 ] para hexadecimal''')
    escolha = int(input("Sua opção: "))

    if escolha == 1:
        print("{} convertido para binario é igual a {}".format(num, bin(num)[2:]))
        break
    elif escolha == 2:
        print("{} convertido para octal é igual a {}".format(num, oct(num)[2:]))
        break
    elif escolha == 3:
        print("{} convertido para hexadecimal é igual a {}".format(num, hex(num)[2:]))
        break
    else:
        print("Digite apenas as opções 1, 2 e 3!!")
        
