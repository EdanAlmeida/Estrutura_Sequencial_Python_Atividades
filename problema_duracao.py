"""
Fazer um programa para ler uma duração de tempo em segundos, daí imprimir na tela esta duração no
formato horas:minutos:segundos.

OBS:
- 1 minuto = 60 segundos
- 1 hora = 60 minutos     = 3600 segundos (60 * 60)

"""

duracao = int(input('Digite a duracao em segundos: '))

horas = duracao//3600
resto = duracao % 3600
minutos = resto // 60
segundos = resto % 60

print(f'{horas}:{minutos}:{segundos}')
