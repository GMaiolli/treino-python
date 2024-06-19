#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase1 = str(input("Digite uma frase: ")).lower().strip()
frase2 = frase1.split()
frase = ''.join(frase2)
n = frase.count('a')
m = frase.find('a')+1
p = frase.rfind('a')+1
print("Sua frase tem {} letras 'A', a primeira letra A aparece na posição {} e a ultima vez aparece na posição {}".format(n, m, p))