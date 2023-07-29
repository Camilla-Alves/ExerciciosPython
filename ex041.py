
from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
if idade <= 9:
    print(f'O atleta tem {idade} anos.\nClassificação: MIRIM')
elif idade <= 14:
    print(f'O atleta tem {idade} anos.\nClassificação: INFANTIL')
elif idade <= 19:
    print(f'O atleta tem {idade} anos.\nClassificação: JÚNIOR')
elif idade <= 25:
    print(f'O atleta tem {idade} anos.\nClassificação: SÊNIOR')
else:
    print(f'O atleta tem {idade} anos.\nClassificação: MASTER')
