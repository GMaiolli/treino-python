def main():
    entrada = input("DIgite Calcular para operações normais(+, -, *, /), para fatorial digite Fat, para calcular raiz quadrada digite Raiz:")
    
    if entrada == 'Raiz':
        numraiz = float(input("Digite o numero que deseja  calcular a raiz quadrada: "))
        print("A raiz quadrada de {} é aproximadamente {:.2f}".format(numraiz, numraiz ** (1/2)))
    
    elif entrada == 'Fat':
        from math import factorial
        n = int(input("Digite o numero que deseja calcular o fatorial:"))
        print("Fatoria de {} é {}".format(n, factorial(n)))
    
    elif entrada == 'Calcular':
        cal = input("DIgite sua conta (usando +, -, *, /):")
        numA, op, numB = cal.split()
        numA = float(numA)
        numB = float(numB)
        
        if op == '+':
            res = numA + numB
            print("Seu resultado é", round(res, 1))
        elif op == '-':
            res = numA - numB
            print("Seu resultado é", round(res, 1))
        elif op == '*':
            res = numA * numB
            print("Seu resultado é", round(res, 1))
        elif op == '/':
            if numB != 0:
                res = numA / numB
                print("Seu resultado é", round(res, 1))
            else:
                print("Não é possivel dividir por zero")
        else:
            print("Operação invalida")

if __name__ == "__main__":
    main()