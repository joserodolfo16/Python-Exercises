frase = str(input('Fale uma frase qualquer: ')).lower().strip()
cont = frase.count('a')
print(f'A letra "a" aparece {cont} vezes.')

prim = frase.find('a' or 'A') + 1
ult = frase.rfind('a' or 'A') + 1
print(f'O primeiro está na {prim}° posição e o último na {ult}° posição.')
