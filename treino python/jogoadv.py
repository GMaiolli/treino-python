import random

x = random.randint(1, 100)

print("Seja bem-vindo ao jogo, esse jogo tente adivinhar qual o numero correto!")

while True:
    numjogador = int(input("Digite um numero de 1 a 100:"))

    if numjogador > x:
        print("Tente um numero menor!")

    elif numjogador < x:
        print("Tente um numero maior!")

    else:
        print(f"Parabens vc acertou o numero correto, que e {x}")
        break