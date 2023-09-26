#Escreva um programa que dê descontos de acordo com o valor da 
#compra: acima de R$100, desconto de 10%; entre R$50 e R$100, 
#desconto de 5%; abaixo de R$50, sem desconto. Calcule e mostre 
#o valor do desconto e o valor total a pagar.

valor_produto = int(input('Preço da compra: '))

if valor_produto > 100:
    valor_produto -= (valor_produto * 0.1)
elif 50 <= valor_produto <= 100:
    valor_produto -= (valor_produto * 0.05)
elif valor_produto < 50:
    valor_produto = valor_produto

print(f'valor total a pagar é R$ {valor_produto}')

