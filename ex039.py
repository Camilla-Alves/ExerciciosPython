import datetime
nascimento = int(input('Ano de nascimento: '))
idade = datetime.date.today().year - nascimento
atraso = idade - 18
adiantado = 18 - idade
ano_alistamento = datetime.date.today().year + adiantado
ano_alistamento_atrasado = datetime.date.today().year - atraso
print(f'Quem nasceu em {nascimento} tem {idade} anos em {datetime.date.today().year}.')
if idade == 18:
    print('Você deverá se alistar IMEDIATAMENTE!')
elif idade == 17:
    print(f'Você deverá se alistar ano que vem!\nSeu alistamento será em {ano_alistamento}.')
elif idade < 18:
    print(f'Você deverá se alistar em {adiantado} anos.\nSeu alistamento será em {ano_alistamento}.')
elif idade == 19:
    print(f'Você deveria ter se alistado ano passado!\nSeu alistamento foi em {ano_alistamento_atrasado}.')
else:
    print(f'Você ja deveria ter se alistado há {atraso} anos!\nSeu alistamento foi em {ano_alistamento_atrasado}.')






