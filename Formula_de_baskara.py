import math

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

delta = b * b - 4 * a * c

if delta < 0:
    print('Impossível dentro dos número reais.')
else:
    xl = (-b + math.sqrt(delta))/(2 * a)
    xl2 = (-b - math.sqrt(delta))/(2 * a)
    print(f'{a}x² + {b}x + {c} = 0')
    print(f'X1 = {xl}\nX2 = {xl2}')
