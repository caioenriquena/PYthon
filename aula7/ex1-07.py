
#Peça ao usuário para inserir o número de horas extras e o número de horas que o funcionário faltou. 
# Se a quantidade de horas extras for maior que as horas faltadas mais 50%, imprima "Bônus de R$ 500.00". 
# Caso contrário, imprima "Sem bônus".


horas = float (input("informe o números de horas extras"))
faltas = float(input("informe a quantidade de horas que faltou"))

metade= faltas / 2

if (metade+faltas) < horas:
    print('Bonus de 500 R$')
else :
    print('Sem bonus')    
