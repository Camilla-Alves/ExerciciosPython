print('=' * 15)
print('BANCO CAMZ')
print('=' * 15)
falta = 0
pago = 0
valor = int(input('Qual valor você quer sacar? R$'))
resto = valor
while True:
     qt_50 = resto // 50
     pago = qt_50 * 50
     if pago > 0:
         print(f'Total de {qt_50} cédula(s) de R$50')
     falta = valor - pago
     if falta == 0:
         break
     else:
         if falta >= 20:
             qt_20 = falta // 20
             pago = qt_20 * 20
             if pago > 0:
                 print(f'Total de {qt_20} cédula(s) de R$20')
             falta -= pago
         if falta == 0:
             break
         else:
             if falta >= 10:
                 qt_10 = falta // 10
                 pago = qt_10 * 10
                 if pago > 0:
                     print(f'Total de {qt_10} cédula(s) de R$10')
                 falta -= pago
             if falta == 0:
                 break
             else:
                 if falta < 10:
                     qt_1 = falta // 1
                     pago = qt_1 * 1
                     if pago > 0:
                         print(f'Total de {qt_1} cédula(s) de R$1')
                     falta -= pago
                 if falta == 0:
                     break
print('=' * 15)
print('Tenha um bom dia e volte sempre!')
