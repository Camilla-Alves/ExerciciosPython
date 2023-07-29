r = 'S'
números = []
while True:
    n = int(input('Digite um valor: '))
    if n in números:
        print('Número duplicado... Não vou adicionar!')
    else:
        números.append(n)
        print('Valor adicionado com sucesso...')
    r = input('Você quer continuar? [S/N] ').upper()
    if r != 'S':
        break
números.sort()
print(f'Você digitou os valores {números}')


