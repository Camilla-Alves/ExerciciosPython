import random
from time import sleep
from operator import itemgetter
valores = {'Jogador1': random.randint(1, 6), 'Jogador2': random.randint(1, 6),
           'Jogador3': random.randint(1, 6), 'Jogador4': random.randint(1, 6)}
ranking = []
print(f'Valores sorteados:')
for k, v in valores.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i + 1}° lugar: {v[0]} com {v[1]}.')
    sleep(1)

