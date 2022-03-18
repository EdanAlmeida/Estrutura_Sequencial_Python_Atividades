"""
Fazer um programa para ler o nome e idade de duas pessoas. Ao final mostrar uma mensagem com os
nomes e a idade média entre essas pessoas, com uma casa decimal, conforme exemplo.
"""

print("Dados da primeira pessoa: ")
nome1 = (input('Nome: '))
idade1 = float(input('Idade: '))
print()
print("Dados da segunda pessoa: ")
nome2 = (input("Nome: "))
idade2 = float(input('Idade: '))

mediaIdade = (idade1 + idade2) / 2

print(f'A idade media de {nome1} e {nome2} e de {mediaIdade} anos')
