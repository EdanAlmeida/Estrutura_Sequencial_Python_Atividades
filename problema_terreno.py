"""
Fazer um programa para ler as medidas da largura e comprimento de um terreno retangular com uma
casa decimal, bem como o valor do metro quadrado do terreno com duas casas decimais. Em seguida,
o programa deve mostrar o valor da área do terreno, bem como o valor do preço do terreno, ambos com
duas casas decimais, conforme exemplo.
"""
largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))
precoM2 = float(input('Digite o valor do metro quadrado R$: '))

area = (largura * comprimento)
precoTerreno = area * precoM2

print(f'Area do terreno: {area:.2f} m2')
print(f'O preco do terreno e: R$ {precoTerreno:.2f}')

