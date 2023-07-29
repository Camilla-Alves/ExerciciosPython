import random
from time import sleep


def sorteia(lista):
    print(f'Sorteando 5 valores da lista: ', end='')
    while len(números) != 5:
        r = random.randint(1, 10)
        if r not in números:
            números.append(r)
    for n in números:
        print(f'{n}', end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for n in números:
        if n % 2 == 0:
            soma += n
    sleep(1)
    print(f'Somando os valores pares de {números}, temos {soma}')


números = []
sorteia(números)
somaPar(números)

