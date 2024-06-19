#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input("Valor da casa: "))
salario = float(input("Salario: "))
anos = int(input("Anos da prestação: "))

mensal = anos * 12
prestacao = valor_casa / mensal

print("Para pagar um imovel de R${:.2f} em {} anos a prestação sera de R${:.2f}".format(valor_casa, anos, prestacao))
if prestacao > salario * 0.3:
    print("Nao foi aprovado o emprestimo")
else:
    print("Foi aprovado o emprestimo")