vogal = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
vogais_corretas = []
consoantes = []

while True:
    frase = input("Digite a frase que você quer saber a quantidade de vogais e consoantes: ")

    
    contador_vogais = 0
    contador_consoantes = 0
    for letra in frase.lower():
        if letra.isalpha() or letra == ' ':
            if letra.isalpha():
                if letra in vogal:
                    contador_vogais += 1

                else:
                    contador_consoantes += 1
                
        else:
            print("Digite apenas letras!")
            break
    else:
        vogais_corretas.append(contador_vogais)
        consoantes.append(contador_consoantes)
        print("A palavra '{}' tem {} vogais e {} consoantes".format(frase, contador_vogais, contador_consoantes))