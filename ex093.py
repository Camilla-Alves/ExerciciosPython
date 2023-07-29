dados = {}
dados['nome'] = str(input('Nome do Jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
dados['gols'] = []
total = 0
for p in range(0, partidas):
    gols = int(input(f'Quantos gols na partida {p + 1}? '))
    dados['gols'].append(gols)
    total += gols
dados['total'] = total
print('-=' * 30)
print(dados)
print('=-' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('=-' * 30)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for p in range(0, partidas):
    print(f'=> Na partida {p + 1}, fez {dados["gols"][p]} gols.')
print(f'Foi um total de {total} gols.')
