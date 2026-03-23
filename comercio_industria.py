# Desenvolver um programa que leia o consumo de água para prédios comerciais e industriais e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 44,95
# Se o consumo for menor ou igual a 20m3, então R$ 8,75 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 16,76 por m3
# Se o consumo for acima dos 50m3, então R$ 17,46 por m3


aguaconsumop=float(input("Digite o consumo de aguá da redisência social em m3:"))

if aguaconsumop <= pow(10, 3) :
    print("O consumo de aguá de seu prédio irá custar R$ 44,95  por m3")

elif aguaconsumop <=  pow(20, 3) : 
     print("O consumo de aguá de seu prédio irá custar R$ 8,75 por m3 ")

elif aguaconsumop <=  pow(50, 3) : 
     print("O consumo de aguá de seu prédio irá custar por R$ 16,76 m3 ")

elif aguaconsumop <=  pow(40, 3) : 
     print("O consumo de aguá de seu prédio irá custar R$6,62 por m3 ")

elif aguaconsumop <=  pow(50, 3) : 
     print("O consumo de aguá de seu prédio irá custar  R$7,31 m3 ")

else:
     print("Seu consumo não se enquadrada em nenhuma das váriaveis possíveis")   
