numero = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif opção == 2:
    print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif opção == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
    print(f'Opção inválida. Tente novamente e digite 1, 2 ou 3.')





