lista = []
lista_pares = []
lista_ímpares = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_ímpares.append(n)
    resposta = input('Quer continuar? [S/N] ').upper()
    if resposta != 'S':
        break
print('-=' * 20)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {lista_pares}')
print(f'A lista de ímpares é {lista_ímpares}')
