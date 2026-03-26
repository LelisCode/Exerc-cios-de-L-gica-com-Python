# Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'

dias = [  #Identificador para cada dia da semana 
    {"id": 1, "semanadia": "Segunda"},
    {"id": 2, "semanadia": "Terça"},
    {"id": 3, "semanadia": "Quarta"},
    {"id": 4, "semanadia": "Quinta"},
    {"id": 5, "semanadia": "Sexta"},
    {"id": 6, "semanadia": "Sábado"},
    {"id": 7, "semanadia": "Domingo"},
]

#Entrada
choseday = int(input("Digite o numero do dia da semana (1-7): ")) 

#processamento
if 1 <= choseday <= 7: #Restrição para retornar um dos valores dentro da lista

    resultado = dias[choseday - 1] #Devido a lista começar por padrão com indíce 0 essa conta é necessária para um output adequado a escolha do usuário
    print(f"O dia escolhido foi: {resultado['semanadia']}") #Saída
else:
    print("Número inválido! Digite entre 1 e 7.") #Saída

             
