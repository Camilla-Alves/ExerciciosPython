# R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de \033[36m{distancia:.1f}km.\033[m')
if distancia > 200:
   preço = distancia * 0.45
else:
   preço = distancia * 0.50
print(f'E o preço da sua passagem será de \033[32m R${preço:.2f}')



