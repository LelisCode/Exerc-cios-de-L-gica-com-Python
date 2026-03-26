#Pergunte o turno da pessoa e retorne uma saudação

print("Escolha uma opção de turno")
print("Opções: M-Matutino, V-Vespertino, N-Noturno")
t=input()



if t == "M":
    tr=("Bom dia!")

elif t == "V":
    tr=("Boa tarde!")

elif t == "N":
    tr=("Boa noite!")

else:
    tr=("Valor inválido!")
  
print(f"{tr}")

