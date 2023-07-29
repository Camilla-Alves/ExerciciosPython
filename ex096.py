def calc_área(a, b):
    área = a * b
    print(f'A área de um terreno de {a}x{b} é de {área}m²')


print('Controle de Terrenos')
print('-' * 20)
a = float(input('LARGURA (m): '))
b = float(input('COMPRIMENTO (m): '))
calc_área(a, b)
