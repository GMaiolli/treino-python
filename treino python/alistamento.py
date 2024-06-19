#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

anonascimento = int(input("Ano de nascimento: "))

idade = 2024 - anonascimento
print("Quem nasceu em {} tem {} anos!".format(anonascimento, idade))
if idade == 18:
    print("Voce deve se alistar imediatamente!!")
elif idade > 18:
    maior = idade - 18
    anoalistamento = 2024 - maior
    if maior == 1:
        print("Voce ja devia ter se alistado ha {} ano".format(maior))
    else:
        print("Voce ja devia ter se alistado ha {} anos".format(maior))
    print("Seu alistamento foi em {}".format(anoalistamento))
else:
    menor = 18 - idade
    anoalistamento = 2024 + menor
    if menor == 1:
        print("Ainda falta {} ano para o alistamento".format(menor))
    else:
        print("Ainda faltam {} anos para o alistamento".format(menor))
    print("Seu alistamento sera em {}".format(anoalistamento))