from random import randint

numero_clientes = 1000
lista_de_respostas = []


while numero_clientes > 0 :

    lista_de_respostas.append(randint(1,5))
    numero_clientes -= 1

respostas1 = lista_de_respostas.count(1)    
respostas2 = lista_de_respostas.count(2)    
respostas3 = lista_de_respostas.count(3)    
respostas4 = lista_de_respostas.count(4)    
respostas5 = lista_de_respostas.count(5)                

print(f'Quantidade de Respostas 1 : {respostas1}')

print(f'Quantidade de Respostas 2 : {respostas2}')

print(f'Quantidade de Respostas 3 : {respostas3}')

print(f'Quantidade de Respostas 4 : {respostas4}')

print(f'Quantidade de Respostas 5 : {respostas5}')

