dados = []
temp_dados = []
maior = menor = 0
while True:
    temp_dados.append(input('Nome: '))
    temp_dados.append(float(input('Peso: ')))
    if len(dados) == 0:
        maior = menor = temp_dados[1]
    else:
        if temp_dados[1] > maior:
            maior = temp_dados[1]
        if temp_dados[1] < menor:
            menor = temp_dados[1]
    dados.append(temp_dados[:])
    temp_dados.clear()
    resp = input('Quer continuar? [S/N] ').upper()
    if resp != 'S':
        break
print('-' * 30)
print(f'Você cadastrou {len(dados)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de ', end='')
for p in dados:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {menor}kg. Peso de ', end='')
for p in dados:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')


