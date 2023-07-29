import random
from time import sleep
print('\033[35m -=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
computador = random.randint(0, 5)  #Faz o computador "PENSAR"
jogador = int(input('Em que número eu pensei? '))  #Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print(f'PARABÉNS, você ganhou! Eu pensei no número {computador}!')
else:
    print(f'PERDEU! Eu pensei no número {computador} e não no {jogador}!')






