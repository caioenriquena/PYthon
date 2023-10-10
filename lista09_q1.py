#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol e armazene os nomes lidos em um vetor (lista). 
# Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de clube e
#  depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), 
# ou NÃO ACHEI caso contrário.

#CRIAR UMA LISTA COM 5 CLUBES


clubes_de_futebol=[
'Internacional',
'Barcelona',
'Flamengo',
'Campinense',
'Atletico de Cabedelo',    

]

#Perguntar qual o clube o usuario vai verificar

clube_pesquisado = input('Digite o clube : ')

for clube in clubes_de_futebol:
    if clube == clube_pesquisado:
        print('Achei')
    else:
        print('Ainda nao encontrei !')    