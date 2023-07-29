import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
cosseno = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print(f'O ângulo de {ângulo} tem o SENO de {seno:.2f}\n O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')


