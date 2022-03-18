"""
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa, conforme exemplo.

"""

nome = input('Nome do funcionario: ')
valorHora = float(input('Valor por hora: R$ '))
horasTrab = float(input('Horas trabalhadas: '))

pagamento = valorHora * horasTrab

print(f'O pagamento para {nome} deve ser: R$ {pagamento:.2f}')
