# Desenvolva um programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem formam um triângulo e se formarem exibir na tela se é equilátero, isósceles ou escaleno.

# Sabemos que:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;



#Entrada
l1 = int(input("Digite o primeiro lado do triângulo: "))
l2 = int(input("Digite o segundo lado do triângulo: "))       
l3 = int(input("Digite o terceiro lado do triângulo: "))  


#Processamento    
if l1 == l2 == l3:  # Uso de == para caso os lados sejam iguais
    t= " Equilátero"
elif l1 != l2 != l3: # Uso de != caso TODOS os lados estiverem diferentes
    t= "Escaleno"
elif l1 != l2 and l1 != l3 and l2 != l3:   # Uso de != para caso aja diferença de lados, and para caso de qualquer um estar certo
    t=" Isósceles"


#Saída
print(f"Seu triângulo é {t}")
