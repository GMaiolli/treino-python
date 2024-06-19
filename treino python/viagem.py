#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input("Digite a distancia da viagem: "))

if viagem <= 200:
    valor1 = viagem * 0.5
    print("Essa viagem ira custar R${:.2f}".format(valor1))

else:
    valor2 = viagem * 0.45
    print("Essa viagem ira custar R${:.2f}".format(valor2))