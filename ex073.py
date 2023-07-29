print ('-=-' * 10)
times = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'RB Bragantino',
         'Fluminense', 'América-MG ', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print(f'Lista de times do Brasileirão 2021: {times}')
print('-=-' * 10)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=-' * 10)
print(f'Os 4 últimos são {times[-4:]}')
print('-=-' * 10)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=-' * 10)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')

