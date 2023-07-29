frase = input('Digite uma frase sem acentos: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if junto == inverso:
    print('Isso é um palíndromo!')
else:
    print('Essa é só uma frase normal...')
