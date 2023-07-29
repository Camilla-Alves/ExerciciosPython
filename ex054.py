from datetime import date
maiores = 0
menores = 0
for i in range(1, 8):
    anos = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idades = date.today().year - anos
    if idades >= 21:
        maiores += 1
    else:
        menores += 1
print(f'Das 7 pessoas informadas, ao todo, {maiores} são maiores de idade e {menores} são menores de idade. ')
