cidade = str(input('Qual o nome da cidade? ')).strip()
resp = cidade.split()
primeira = resp[0].lower()
print('Existe "Santo" no começo da cidade? ')
print('santo' in primeira)