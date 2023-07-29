import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.date.today().year - ano_nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
    ano_contrat = int(input('Ano de Contratação: '))
    dados['contratação'] = ano_contrat
    salário = float(input('Salário: R$'))
    dados['salário'] = salário
    idade_contrat = ano_contrat - ano_nasc
    idade_aposent = idade_contrat + 35
    dados['aposentadoria'] = idade_aposent
print('-=' * 20)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')

