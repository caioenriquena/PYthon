# Inicialize uma lista vazia para armazenar os números que atendem à condição
numeros_que_atendem = []

# Loop de 1000 a 2000
for numero in range(1000, 2001):
    # Verifique se o resto da divisão por 11 é igual a 5
    if numero % 11 == 5:
        # Se sim, adicione o número à lista
        numeros_que_atendem.append(numero)

# Imprima os números que atendem à condição
print("Números entre 1000 e 2000 que divididos por 11 têm resto igual a 5:")
for numero in numeros_que_atendem:
    print()
    print(numero)
