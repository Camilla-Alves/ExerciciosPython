time = []
jogador = {}
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do Jogador: '))
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    jogador['gols'] = []
    total = 0
    for p in range(0, partidas):
        gols = int(input(f'Quantos gols na partida {p + 1}? '))
        jogador['gols'].append(gols)
        total += gols
    jogador['total'] = total
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print(f'cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f' => No jogo {i + 1} fez {g} gols.')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
