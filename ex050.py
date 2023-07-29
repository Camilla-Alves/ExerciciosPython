soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i} valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma dos {cont} valores pares foi {soma}')

