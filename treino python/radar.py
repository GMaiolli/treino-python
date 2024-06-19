#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velo = int(input("Digite a velocidade: "))

if velo > 80:
    newvelo = velo - 80
    multa = newvelo * 7
    print("Voce ultrapassou o limite de 80Km/h, excedeu {}Km/h da velocidade permitida, portando sua multa sera de R${:.2f}".format(newvelo, multa))
else:
    print("Esta dentro do limite da via!")