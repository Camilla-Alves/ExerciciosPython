print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima \033[32m PODEM FORMAR \033[m um triângulo!')
else:
    print('Os segmentos acima \033[31m NÃO PODEM FORMAR \033[m um triângulo!')


