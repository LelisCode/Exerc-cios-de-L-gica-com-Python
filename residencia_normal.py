# Desenvolver um programa que leia o consumo de água para uma residência normal e exiba o valor (R$) da conta baseado nos seguintes cálculos:
# Se o consumo for menor ou igual a 10m3, então R$ 22,38
# Se o consumo for menor ou igual a 20m3, então R$ 3,50 por m3
# Se o consumo for menor ou igual a 50m3, então R$ 8,75 por m3
# Se o consumo for acima dos 50m3, então R$ 9,64 por m3

consumon= float(input("Digite o consumo de aguá da sua redisência em m3:"))

 
if consumon <= pow(10, 3):
    valor = consumon * 22.38
    
elif consumon <=  pow(20, 3): 
     valor = consumon * 3.50
elif consumon <=  pow(50, 3): 
     valor = consumon * 8.75
else:
     valor = consumon * 9.64

print(f"O consumo de água de sua residência irá custar R$ {valor:.2f}")
