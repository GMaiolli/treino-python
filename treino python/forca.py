import random

palavras = ['abacaxi', 'abelha', 'academia', 'acolhedor', 'amizade', 'anel', 'antena', 'apartamento', 'areia', 'armadilha', 'atmosfera', 'avestruz', 'avião', 'bala', 'banheira', 'barco', 'batom', 'biblioteca', 'bicicleta', 'bloco', 'bolacha', 'borboleta', 'brigadeiro', 'cadeira', 'cachorro', 'caderno', 'café', 'camelo', 'camiseta', 'caneta', 'carambola', 'carne', 'carrinho', 'carro', 'cego', 'celular', 'chave', 'chocolate', 'chuva', 'cinema', 'circo', 'cidade', 'cinto', 'cobra', 'computador', 'coração', 'corrida', 'dado', 'dança', 'degrau', 'dente', 'desenho', 'diamante', 'dicionário', 'disco', 'doce', 'dragão', 'elefante', 'estrela', 'estufa', 'família', 'farmácia', 'festa', 'flor', 'foguete', 'formiga', 'fotografia', 'fruta', 'gafanhoto', 'galáxia', 'garrafa', 'gato', 'geladeira', 'girafa', 'golfinho', 'helicóptero', 'hiena', 'hipopótamo', 'hospital', 'hotel', 'iguana', 'ilha', 'janela', 'jipe', 'joaninha', 'jornal', 'lagartixa', 'laranja', 'leão', 'livro', 'maçã', 'mala', 'máscara', 'melancia', 'motocicleta', 'nave', 'notebook', 'nuvem', 'oceano']

pal = random.choice(palavras)

sublinhados = '_ ' * len(pal)

print("Advinhe qual a palavra:")

print()

print(sublinhados)

letras_corretas = []
letras_erradas = []

while True:
    letra = input("Digite uma letra: ").lower()  
    
    if letra in letras_corretas:
        print("Você já escolheu esta letra. Tente outra.")
        continue
    elif letra in letras_erradas:
        print("Você já escolheu esta letra. Tente outra.")
        continue
    
    if letra in pal:
        letras_corretas.append(letra)  
        print("Letra correta!")
    else:
        letras_erradas.append(letra)
        print("Letra incorreta!")
    
    palavra_mostrada = ''
    for letra_palavra in pal:
        if letra_palavra in letras_corretas:
            palavra_mostrada += letra_palavra + ' '
        else:
            palavra_mostrada += '_ '
    print("Palavra:", palavra_mostrada.strip())
    
    if all(letra in letras_corretas for letra in pal):
        print("Parabéns! Você ganhou!")
        break