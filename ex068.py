import random
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
sequência_vítorias = 0
while True:
    total = 0
    pc = random.choice(range(1, 11))
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I]? ')).upper()
    print('-' * 45)
    total = jogador + pc
    print(f'Você jogou {jogador} e o computador {pc}. Total de {total}')
    print('-' * 45)
    if total % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    print(f'DEU {resultado}')
    if escolha == 'P':
        escolha = 'PAR'
    elif escolha == 'I':
        escolha = 'ÍMPAR'
    if escolha == resultado:
        print('Você VENCEU!\nVamos jogar novamente...')
        sequência_vítorias += 1
        print('=-' * 15)
    else:
        break
print('Você PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {sequência_vítorias} vezes.')



