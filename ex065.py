continuar = 'S'
soma = contagem = média = maior = menor = 0
while continuar == 'S':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    soma += num
    contagem += 1
    if contagem == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / contagem
print(f'Você digitou {contagem} números e a média foi {média:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')



