from time import sleep
v1 = float(input('Primeiro valor: '))
v2 = float(input('Segundo valor: '))
opção = 0
while opção != 5:
    soma = v1 + v2
    mult = v1 * v2
    maior = v1
    print('=-=' * 17)
    menu = print('''             [ 1 ] somar
             [ 2 ] multiplicar
             [ 3 ] maior
             [ 4 ] novos números
             [ 5 ] sair do programa''')
    opção = int(input('>>>>>> Qual é a sua opção? '))
    if opção == 4:
        v1 = float(input('Primeiro valor: '))
        v2 = float(input('Segundo valor: '))
    elif opção == 1:
        print(f'O resultado da soma entre {v1} e {v2} é {soma}')
    elif opção == 2:
        print(f'O resultado da multiplicação entre {v1} e {v2} é {mult}')
    elif opção == 3:
        if v2 > v1:
            print(f'O maior número é {v2}')
        else:
            print(f'O maior número é {v1}')
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    sleep(2)
print('Fim do programa, Volte sempre!')



