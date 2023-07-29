while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 40)
    if n < 0:
        break
    for i in range(0, 11):
        print(f'{n} x {i:2} = {n * i}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. VOLTE SEMPRE!')
