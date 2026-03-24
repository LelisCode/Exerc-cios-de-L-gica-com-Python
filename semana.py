# Desenvolver um programa que leia um número de 1 a 7 e exiba o dia da semana:
#    1 - 'Domingo'
#    2 - 'Segunda'
#    3 - 'Terça'
#    4 - 'Quarta'
#    5 - 'Quinta'
#    6 - 'Sexta'
#    7 - 'Sábado'

dias = [
    {"id": 1, "semanadia": "Segunda"},
    {"id": 2, "semanadia": "Terça"},
    {"id": 3, "semanadia": "Quarta"},
    {"id": 4, "semanadia": "Quinta"},
    {"id": 5, "semanadia": "Sexta"},
    {"id": 6, "semanadia": "Sábado"},
    {"id": 7, "semanadia": "Domingo"},
]

choseday = int(input("Digite o numero do dia da semana (1-7): "))

if 1 <= choseday <= 7:

    resultado = dias[choseday - 1]
    print(f"O dia escolhido foi: {resultado['semanadia']}")
else:
    print("Número inválido! Digite entre 1 e 7.")

             
