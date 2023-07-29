Soma_Idade = 0
Maior_M = 0
Nome_Maior_M = ''
Idade_F = 0
for p in range(1, 5):
    print(f'---- {p}ª PESSOA ----')
    Nome = input('Nome: ')
    Idade = int(input('Idade: '))
    Sexo = input('Sexo [M/F]: ').upper()
    Soma_Idade += Idade
    Média_Idade = Soma_Idade / 4
    if Sexo == 'M'.upper():
        if p == 1:
            Maior_M = Idade
            Nome_Maior_M = Nome
        else:
            if Idade > Maior_M:
                Maior_M = Idade
                Nome_Maior_M = Nome
    else:
        if Idade < 20:
            Idade_F += 1
print(f'A Média de idade do grupo é de {Média_Idade} anos')
print(f'O homem mais velho tem {Maior_M} anos e se chama {Nome_Maior_M}')
print(f'Ao todo são {Idade_F} mulher/mulheres com menos de 20 anos')

