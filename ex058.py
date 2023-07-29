from time import sleep
import random
print('\033[35m-=-' * 33)
print('Olá, sou seu computador! Vou pensar em um número entre 0 e 10. Vamos ver se você consegue acertar!')
print('-=-' * 33)
jogador = -1
jogadas = 0
demora = ''
computador = random.randint(0, 10)  #Faz o computador "PENSAR"
while jogador != computador:
    jogador = int(input('Em que número eu pensei? '))  # Jogador tenta adivinhar
    jogadas += 1
    if jogador > computador:
        print('Menos...Tente novamente')
    elif jogador < computador:
        print('Mais...Tente novamente')
print('PROCESSANDO...')
sleep(1)
if jogadas > 5:
    demora = 'Demorou hein! Pensei que você não ia acertar nunca!'
elif jogadas == 1:
    demora = 'De primeira! Acho que você sabe ler mentes...'
else:
    demora = 'Parabéns! Isso foi mais rápido do que eu estava esperando...'
print(f'Acertou com {jogadas} tentativa(s). {demora}')
