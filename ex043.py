#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f}. Você está ABAIXO DO PESO normal!')
elif imc < 25:
    print(f'Seu IMC é de {imc:.1f}. Parabéns, você está na faixa de PESO IDEAL!')
elif imc < 30:
    print(f'Seu IMC é de {imc:.1f}. Você está em SOBREPESO!')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.1f}. Você está em OBESIDADE!')
else:
    print(f'Seu IMC é de {imc:.1f}. Você está em OBESIDADE MÓRBIDA, cuidado!')
    







