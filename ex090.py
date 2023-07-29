alunos = {}
nome = str(input('Nome: '))
média = float(input('Média do aluno: '))
alunos['nome'] = nome
alunos['média'] = média
if média < 5:
    alunos['situação'] = 'Reprovado'
elif média < 7:
    alunos['situação'] = 'Recuperação'
else:
    alunos['situação'] = 'Aprovado'
print('-=' * 20)
for k, v in alunos.items():
    print(f'{k} é igual a {v}')


