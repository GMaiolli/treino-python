tax1 = 1.2
tax2 = 1.17
tax3 = 1.6

valorfinal = 0
taxafinal = 0

entrada = float(input("Digite o valor do produto em reais: "))

if entrada < 268:
    valorfinal = entrada * tax1 * tax2
    

elif entrada >= 268:
    valorfinal = entrada * tax1 * tax3
    
taxafinal = valorfinal - entrada
print("Seu protudo custa ", round(valorfinal, 2), "pois teve uma taxa cobrada de:", round(taxafinal, 2))