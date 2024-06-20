import math

a = float(input("Digite o valor da reta 1: "))
b = float(input("Digite o valor da reta 2: "))
c = float(input("Digite o valor da reta 3: "))

if b - c < a < b + c and a - c < b < a + c and b - a < c < b + a:
    
    angulo_A = math.acos((b**2 + c**2 - a**2) / (2 * b * c))
    angulo_B = math.acos((a**2 + c**2 - b**2) / (2 * a * c))
    angulo_C = math.acos((a**2 + b**2 - c**2) / (2 * a * b))

    angulo_A = math.degrees(angulo_A)
    angulo_B = math.degrees(angulo_B)
    angulo_C = math.degrees(angulo_C)
    
    print("Ângulos do triângulo:")
    print("Ângulo A: {:.2f}°".format(angulo_A))
    print("Ângulo B: {:.2f}°".format(angulo_B))
    print("Ângulo C: {:.2f}°".format(angulo_C))

    if a == b == c:
        print("As retas {} {} {} formam um triangulo equilátero!".format(a, b, c))
    elif a == b or a == c or b ==c:
        print("As retas {} {} {} formam um triangulo isósceles!".format(a, b, c))
    else:
        print("As retas {} {} {} formam um triangulo escaleno".format(a, b, c))

else:
    print("nao eh um triangulo")