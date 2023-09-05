#Exercício 3: Calcular a soma de todos os números ímpares de 1 a 100 com um loop while
numero = 1
soma = 0

while numero <= 100:
    if numero % 2 != 0:  # Verifica se o número é ímpar
        soma += numero
    numero += 1

print("A soma dos números ímpares de 1 a 100 é:", soma)
