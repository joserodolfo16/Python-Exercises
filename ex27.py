nome = str(input('Nome completo: ')).strip().split()
print(f'O primeiro nome é {nome[0]}.')
print('O último nome é {}.'.format(nome[len(nome)-1]))
