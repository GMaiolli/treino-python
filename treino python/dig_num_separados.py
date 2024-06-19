num = int(input("Digite um numero de 0 a 9999:"))

if num > 9999 or num < 0:
    print("Apenas numeros entre 0 e 9999")
else:
    print("Unidade: \033[31m{}\033[m".format(num // 1 % 10))
    print("Dezena: \033[34m{}\033[m".format(num // 10 % 10))
    print("Centena: \033[35m{}\033[m".format(num // 100 % 10))
    print("Milhar: \033[36m{}\033[m".format(num // 1000 % 10))