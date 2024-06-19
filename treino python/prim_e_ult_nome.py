#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente

nome = str(input("Digite seu nome:")).strip()
nomesep = nome.split()
print("Seu primeiro nome: {}".format(nomesep[0]))
print("Seu ultimo nome: {}".format(nomesep[len(nomesep)-1]))