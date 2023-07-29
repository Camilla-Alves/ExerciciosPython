#salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario = float(input('Qual é o salário do funcionário? R$'))
if salario <= 1250:
    novo = salario + 15/100 * salario
else:
    novo = salario + 10/100 * salario
print(f'Quem ganhava \033[33mR${salario:.2f} \033[m passa a ganhar \033[32mR${novo:.2f} \033[m agora.')




