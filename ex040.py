#– Média abaixo de 5.0: REPROVADO

# Média entre 5.0 e 6.9: RECUPERAÇÃO

# Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    situação = 'REPROVADO'
elif m >= 7:
    situação = 'APROVADO'
else:
    situação = 'em RECUPERAÇÃO'
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {m:.1f}\nO aluno está {situação}.')





