def ficha(jog='<desconhecido>', gol=0):
    print('-' * 40)
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = input('Nome do jogador: ')
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)