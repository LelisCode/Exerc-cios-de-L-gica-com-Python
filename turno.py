#Pergunte o turno da pessoa e retorne uma saudação

#Entrada
print("Escolha uma opção de turno")
print("Opções: M-Matutino, V-Vespertino, N-Noturno")
t=input()


#Processamento
if t == "M":  #Aqui será a entrada do turno matutino
    tr=("Bom dia!")

elif t == "V":  #Aqui será a entrada do turno Vespertino
    tr=("Boa tarde!")

elif t == "N":  #Aqui será a entrada do turno Noturno
    tr=("Boa noite!")

else:     #Caso a pessoa não escolha nenhuma das opções esse será seu retorno
    tr=("Valor inválido!")
#Saída  
print(f"{tr}")

