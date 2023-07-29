divs = 0
resultado = ' '
n = int(input('Digite um número: '))
for i in range(1, n + 1):
    if n % i == 0:
        divs += 1
        if divs == 2:
            resultado = 'É PRIMO'
        else:
            resultado = 'NÃO É PRIMO'
print(f'O número {n} foi divisível {divs} vezes')
print(f'E por isso ele {resultado}')




