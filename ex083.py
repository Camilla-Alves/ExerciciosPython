p = []
teste = input('Digite uma expressão matemática: ')
for i in teste:
    if i == '(':
        p += i
    elif i == ')':
        p += i
if len(p) > 0:
    if len(p) % 2 == 0:
        print('Sua expressão está válida!')
    else:
        print('Sua expressão está errada!')
else:
    print('Isso não é uma expressão matemática.')

    #Método mais efetivo e correto:
'''expr = str(input('Digite a expressão: '))
   p = []
   for símb in expr:
   if símb == '(':
        p.append('(')
   elif símb == ')':
        if len(p) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão está válida!'
else:
    print('Sua expressão está errada!')
    '''