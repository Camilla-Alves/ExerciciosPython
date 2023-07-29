import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista_de_alunos = [a1, a2, a3, a4]
print(f'O aluno escolhido foi {random.choice(lista_de_alunos)}')
#sorteio
