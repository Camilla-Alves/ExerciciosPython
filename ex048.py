soma = 0
contador = 0
for i in range(1, 501):
    if i % 2 == 1:
      if i % 3 == 0:
          contador += 1
          soma += i
print(f'A soma de todos os {contador} valores é {soma}')












