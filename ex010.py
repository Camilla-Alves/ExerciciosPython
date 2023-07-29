real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = 1*real / 5.21
euro = 1*real / 5.55
print(f'Com R${real:.2f} você pode comprar US${dolar:.2f} e €{euro:.2f}')

