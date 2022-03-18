"""
Fazer um programa para ler três medidas A, B e C. Em seguida, calcular e mostrar (imprimir os dados
com quatro casas decimais):
a) a área do quadrado que tem lado A
b) a área do triângulo retângulo que base A e altura B
c) a área do trapézio que tem bases A e B, e altura C

"""

a = float(input('Digite a medida de A: '))
b = float(input('Digite a medida de B: '))
c = float(input('Digite a medida de C: '))

areaQuadrado = a * a
areaTriangulo = (a * b) / 2
areaTrapezio = ((a + b) * c) / 2

print(f'AREA DO QUADRADO: {areaQuadrado:.4f}')
print(f'AREA DO TRIANGULO: {areaTriangulo:.4f}')
print(f'AREA DO TRAPEZIO: {areaTrapezio:.4f}')
