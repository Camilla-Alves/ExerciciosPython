import random
import time
print('-=-'*5, 'JOKENPÔ', '-=-'*5)
print('Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
jogador = int(input('Qual é a sua jogada? '))
if jogador == 0:
    jogador = 'PEDRA'
if jogador == 1:
    jogador = 'PAPEL'
if jogador == 2:
    jogador = 'TESOURA'
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('-=-'*8)
opções = ['PEDRA','PAPEL','TESOURA']
pc = random.choice(opções)
print(f'Computador jogou {pc}\nJogador jogou {jogador}')
print('-=-'*8)
if jogador == pc:
    print('EMPATE')
elif jogador == 'PEDRA' and pc == 'PAPEL':
    print('COMPUTADOR VENCE')
elif jogador == 'PEDRA' and pc == 'TESOURA':
    print('JOGADOR VENCE')
elif jogador == 'PAPEL' and pc == 'PEDRA':
    print('JOGADOR VENCE')
elif jogador == 'PAPEL' and pc == 'TESOURA':
    print('COMPUTADOR VENCE')
elif jogador == 'TESOURA' and pc == 'PEDRA':
    print('COMPUTADOR VENCE')
elif jogador == 'TESOURA' and pc == 'PAPEL':
    print('JOGADOR VENCE')
else:
    print('ERRO! JOGADA INVÁLIDA!')
    








