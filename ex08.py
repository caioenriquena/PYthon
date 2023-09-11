# Criando um app de carrinho de supermercado



comidas = []
precos = []
total = 0

while True:
    comida = input("Digite a comida que deseja  (q para sair): ")
    if comida.lower() == "q":
        break
    else:
        preco = float(input(f"Diga o preço do alimento :  {comida}: R$"))
        comidas.append(comida)
        precos.append(preco)

print("----- Seu Carrinho -----")

for comida in comidas:
    print(comida, end=" ")

for preco in precos:
    total += preco

print()
print(f"Seu total é  R${total}")