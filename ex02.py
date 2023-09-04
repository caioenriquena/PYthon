'''usuario= float(input('Escreva o número : '))

print(f'Número escolhido é : {usuario}')

if usuario > 10 :

  print("valor é  maior ")

else:
  print("valor é menor")  '''

#Escreva duas notas de avaliação (EX 02)

nota_1 = float(input("nota 1 é : "))
nota_2 = float(input("nota 2 é : "))

#Calculo da média 

media = (nota_1+nota_2) / 2


if (6 <= media <= 10 ):
    print(f'Aluno Aprovado com média  {media}')
elif 0 <= media <6 :
    print(f'Aluno Reprovado com média {media} ')  
else:
    print(f'valor da média inválido -> {media}')      