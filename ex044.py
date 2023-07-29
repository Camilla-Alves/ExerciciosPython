print('='*20, 'LOJAS CAMILLA', '='*20)
compras = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO\n[ 1 ] á vista dinheiro/cheque\n[ 2 ] á vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão')
pagamento = int(input('Qual é a opção? '))
if pagamento == 1:                           #à vista dinheiro/cheque: 10% de desconto
    valor_final = compras - 10/100 * compras
elif pagamento == 2:                         #à vista no cartão: 5% de desconto
    valor_final = compras - 5/100 * compras
elif pagamento == 3:                         #em até 2x no cartão: preço normal
    parcelas = 2
    valor_final = compras
    valor_parcela = compras / parcelas
    print(f'Sua compra será parcelada em 2x de R${valor_parcela:.2f} SEM JUROS')
elif pagamento == 4:                        #3x ou mais no cartão: 20% de juros
    parcelas = int(input('Quantas parcelas? '))
    valor_final = compras + 20/100 * compras
    valor_parcela = valor_final / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${valor_parcela:.2f} COM JUROS')
else:
    valor_final = compras
    print('ERRO! Tente novamente e informe uma forma de pagamento válida.')
print(f'Sua compra de R${compras:.2f} vai custar R${valor_final:.2f} no final.')










