# R$60 por dia e R$0,15 por Km rodado
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
total = 60 * dias + 0.15 * km
print(f'O total a pagar é de R${total:.2f}')

