frase = str(input('Digite uma frase: ')).strip().upper()
vezes = int(frase.count('a') + frase.count('A'))
print(f'A letra A aparece {vezes} vezes na frase.')
primeira = (frase.find('A')+1)
#if primeira == 0:
#    resultado = 0 + 1
#else:
    #resultado = primeira
print(f'A primeira letra A apareceu na posição {primeira}')
ultima = (frase.rfind('A')+1)
print(f'A última letra A apareceu na posição {ultima}')



