import math
cat_op = float(input('Comprimento do cateto oposto: '))
cat_adj = float(input('Comprimento do cateto adjacente: '))
hip = math.hypot(cat_op, cat_adj)
print(f'A hipotenusa vai medir {hip:.2f}')
