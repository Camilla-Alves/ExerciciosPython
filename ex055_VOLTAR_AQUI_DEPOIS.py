maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O menor peso lido foi de {menor:.1f}Kg e o maior foi de {maior:.1f}Kg')

'''Um jeito mais simples que consegui fazer:
lst=[]  #lista vazia
for c in range(1, 6):
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lst+=[peso]   #adc os valores de peso na lista
print('')
print('O Maior peso foi:', max(lst))  #maximo valor da lista
print('O Menor peso foi:', min(lst))  #minimo valor da list'''

'''
Fiz quase idêntico, mas com um sort pra ordenar e depois imprimir as posições 0 e 4. 
pesos = []
for i in range(1,6):
    peso = float(input(f"Qual o peso da {i}ª pessoa? "))
    pesos += [peso]
pesos.sort()
print(f'O maior peso lido foi de {pesos[4]} Kg e o menor peso foi de {pesos[0]}')'''