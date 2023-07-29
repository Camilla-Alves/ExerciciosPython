#A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
valor = float(input('Valor da casa: R$'))
salario = float(input('Sálario do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = valor / (anos * 12)
print(f'Para pagar uma casa de \033[1;32mR${valor:.2f}\033[m em \033[1;33m{anos} anos\033[m a prestação será de \033[4;32mR${prestação:.2f}\033[m')
if prestação > 30/100 * salario:
    print('\033[31mEmpréstimo NEGADO!, prestação excedeu 30% do valor de seu salário mensal.\033[m')
else:
    print('\033[32mEmpréstimo APROVADO!')


