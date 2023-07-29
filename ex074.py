from random import randint
cont = 0
sorteio = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end='')
for n in sorteio:
    print(n, end=' ')
    cont += 1
    if cont == 1:
        menor = n
        maior = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
print(f'\nO maior valor sorteado foi {maior}\nO menor valor sorteado foi {menor}')
# Solução mais simples para ver o maior e o menor valor de uma Tupla.
#print(f'O maior valor sorteado foi {max(sorteio)}')
#print(f'O menor valor sorteado foi {min(sorteio)}')
