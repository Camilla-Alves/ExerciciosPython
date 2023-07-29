print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais_vezes = 10
while mais_vezes != 0:
    total += mais_vezes
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais_vezes = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {cont - 1} termos mostrados')
