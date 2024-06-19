import random

def jogo_multiplicacao():
    pontuacao = 0
    num_perguntas = 5  
    
    print("Bem-vinda ao jogo de multiplicação!")
    print("Responda corretamente para ganhar pontos.")
    print("Vamos começar!\n")
    
    for _ in range(num_perguntas):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        
        resposta_correta = num1 * num2
        
        print(f"Quanto é {num1} x {num2}?")
        try:
            resposta_jogador = int(input("Resposta: "))
        except ValueError:
            print("Por favor, digite um número válido.")
            continue
        
        if resposta_jogador == resposta_correta:
            print("Resposta correta!")
            pontuacao += 10
        else:
            print(f"Resposta incorreta. A resposta correta era {resposta_correta}.")
            pontuacao -= 5
        
        print()  
    
    print(f"Fim do jogo! Sua pontuação total é: {pontuacao}")

jogo_multiplicacao()