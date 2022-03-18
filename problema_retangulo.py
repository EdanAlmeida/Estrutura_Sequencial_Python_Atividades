"""
Fazer um programa para ler as medidas da base e altura de um retângulo. Em seguida, mostrar o valor
da área, perímetro e diagonal deste retângulo, com quatro casas decimais, conforme exemplos.
"""
import math

base = float(input('Base do retangulo: '))
altura = float(input('Altura retangulo: '))

area = base * altura
perimetro = 2 * (base + altura)
diagonal = math.sqrt((altura ** 2) + (base ** 2))

print(f'Area: {area:.4f}')
print(f'Perimetro: {perimetro:.4f}')
print(f'Diagonal: {diagonal:.4f}')