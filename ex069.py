print('-' * 25)
print('CADASTRE UMA PESSOA')
print('-' * 25)
maiores = homens = mulheres_novas = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).upper()
    if idade > 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_novas += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
    print('-' * 25)
    if continuar == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maiores} ')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres_novas} mulher(es) com menos de 20 anos')