aluno = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    aluno.append([nome, [nota1, nota2], média])
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar != 'S':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, a in enumerate(aluno):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-' * 35)
    opção = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(aluno) - 1:
        print(f'Notas de {aluno[opção][0]}: {aluno[opção][1]}')
print('<<< VOLTE SEMPRE >>>')




