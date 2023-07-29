import time
import random
print('-' * 30)
print(f'     JOGOS PARA MEGA SENA      ')
print('-' * 30)
jogo = []
jogadas = int(input('Quantos jogos você quer sortear? '))
print(f'>>>>>> SORTEANDO {jogadas} JOGOS... <<<<<<')
time.sleep(2)
for j in range(1, jogadas + 1):
    jogo = random.sample(range(1, 60), 6)
    jogo.sort()
    print(f'Jogo {j}: {jogo}')
    time.sleep(1)
print('>>>>>>>>>> BOA SORTE! <<<<<<<<<<')
