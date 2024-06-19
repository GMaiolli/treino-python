import math

angulo = float(input("Digite o angulo que deseja calcular o sen, cos e tg: "))

sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tg = math.tan(math.radians(angulo))

print("sen {:.4f} cos {:.4f} tg {:.4f}".format(sen, cos, tg))