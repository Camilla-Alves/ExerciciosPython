nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...')
print(f'Seu nome em maiúsculas é {(nome.upper())}')
print(f'Seu nome em minúsculas é {(nome.lower())}')
print('Seu nome ao todo tem {} letras'.format(len(nome) - nome.count(' ')))
dividido = (nome.split())
print(f'Seu primeiro nome é {(dividido[0])} e ele tem {(len(dividido[0]))} letras')



