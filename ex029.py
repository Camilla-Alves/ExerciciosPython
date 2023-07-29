velocidade = float(input('Qual é a velocidade atual do carro? '))
limite = 80
if velocidade > limite:
    multa = (velocidade - limite) * (+7)
    print(f'\033[1;31m MULTADO! Você excedeu o limite permitido que é de 80km/h\nVocê deve pagar uma multa de \033[4;31mR${multa:.2f}!\033[m')
print('\033[1;33m Tenha um bom dia! Dirija com segurança!')
