"""
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente.
"""

precoUni = float(input("Preco unitario do produto: R$ "))
quantidade = int(input("Quantidade Comprada: "))
dinheiro = float(input("DInheiro recebido: R$ "))

troco = dinheiro - (precoUni * quantidade)

print(f'TROCO: R$ {troco:.2f}')
