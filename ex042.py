#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferente
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a == b == c:
    print(f'Os segmentos acima \033[32m PODEM FORMAR \033[m um triângulo EQUILÁTERO')
elif a == b or b == c or c == a:
    print(f'Os segmentos acima \033[32m PODEM FORMAR \033[m um triângulo ISÓSCELES')
elif a + b > c and a + c > b and b + c > a:
    print(f'Os segmentos acima \033[32m PODEM FORMAR \033[m um triângulo ESCALENO')
else:
    print('Os segmentos acima \033[31m NÃO PODEM FORMAR \033[m um triângulo!')

