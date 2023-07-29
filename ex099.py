from time import sleep


def Maior(* números):
    print('-=' * 20)
    print(f'Analisando os valores passados...')
    sleep(3)
    if números == ():
        print(f'Foram informados 0 valores ao todo')
        print(f'O maior valor informado foi 0.')
    else:
        for núm in números:
            print(f'{núm}', end=' ')
            sleep(0.5)
        print(f'Foram informados {len(números)} valores ao todo')
        for núm in números:
            if núm == max(números):
                maior = núm
                print(f'O maior valor informado foi {maior}.')


Maior(3, 4, 6, 7, 20, 40, 36)
Maior(67, 89, 120, 45, 107)
Maior(2, 5, 1)
Maior(78, 65)
Maior(9)
Maior()
