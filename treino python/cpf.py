cpf = input("Digite seu cpf: ")

cpflimpo = cpf.replace('.', '').replace('-', '')

if len(cpflimpo) != 11:
    print("Cpf Invalido!")
else:
    soma1 = (int(cpflimpo[0]) * 10) + (int(cpflimpo[1]) * 9) + (int(cpflimpo[2]) * 8) + (int(cpflimpo[3]) * 7) + (int(cpflimpo[4]) * 6) + (int(cpflimpo[5]) * 5) + (int(cpflimpo[6]) * 4) + (int(cpflimpo[7]) * 3) + (int(cpflimpo[8]) * 2)

    resto1 = soma1 % 11
    if resto1 < 2:
        penultimodig = 0
    else:
        penultimodig = 11 - resto1

    if penultimodig == int(cpflimpo[9]):
        soma2 = (int(cpflimpo[0]) * 11) + (int(cpflimpo[1]) * 10) + (int(cpflimpo[2]) * 9) + (int(cpflimpo[3]) * 8) + (int(cpflimpo[4]) * 7) + (int(cpflimpo[5]) * 6) + (int(cpflimpo[6]) * 5) + (int(cpflimpo[7]) * 4) + (int(cpflimpo[8]) * 3) + (int(cpflimpo[9]) * 2)
        resto2 = soma2 % 11
        if resto2 < 2:
            ultimodig = 0
        else:
            ultimodig = 11 - resto2
        if ultimodig != int(cpflimpo[10]):
            print("Cpf Invalido!")
        else:
            print("Cpf Valido!")
    else:
        print("Cpf Invalido!")