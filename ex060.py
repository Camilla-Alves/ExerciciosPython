#import math
#num = int(input('Digite um número: '))
#fat = math.factorial(num)
#print(f'O fatorial de {num} é {fat}')
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print(f'Calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')
