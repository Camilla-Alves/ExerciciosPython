def voto(ano_nasc):
    import datetime
    idade = datetime.date.today().year - ano_nasc
    if idade > 70:
        situação = 'VOTO OPCIONAL'
    elif idade >= 18:
        situação = 'VOTO OBRIGATÓRIO'
    elif idade >= 16:
        situação = 'VOTO OPCIONAL'
    elif idade < 16:
        situação = 'NÃO VOTA'
    print(f'Com {idade} anos: {situação}.')


ano_nasc = int(input('Ano de nascimento: '))
voto(ano_nasc)
