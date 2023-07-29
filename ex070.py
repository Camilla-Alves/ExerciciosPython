print('-' * 25)
print('LOJINHA DA CAMILLINHA')
print('-' * 25)
total = produtos_caros = mais_barato = cont = 0
nome_barato = ''
while True:
    nome = str(input('Nome do Produto: ')).upper()
    preço = float(input('Preço: R$'))
    cont += 1 # É NECESSÁRIO POR UM CONTADOR PARA VERIFICAR SE ESTAMOS REGISTRANDO O PRIMEIRO PRODUTO ANTES DE POR O MAIS BARATO RECEBENDO O PREÇO
    if cont == 1 or preço < mais_barato: #FORMA DE SIMPLIFICAR E USAR MENOS LINHAS
        mais_barato = preço
        nome_barato = nome
    if preço > 1000:
        produtos_caros += 1
    total += preço
    continuar = str(input('Quer continuar? [S/N] ')).upper()
    if continuar == 'N':
        break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {produtos_caros} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_barato} que custa R${mais_barato:.2f}')
