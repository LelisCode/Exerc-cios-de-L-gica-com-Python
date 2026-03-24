# Desenvolva um programa que exiba na tela um menu de opções:

#    1 - Opção 1
#    2 - Opção 2
#    3 - Opção 3
#    4 - Sair
#    Digite uma opção: 
# Se o usuário digitar 1, exibir na tela: 'Você selecionou a opção 1'
# Se o usuário digitar 2, exibir na tela: 'Você selecionou a opção 2'
# Se o usuário digitar 3, exibir na tela: 'Você selecionou a opção 3'
# Se o usuário digitar 4, exibir na tela: 'Você selecionou sair'
# Se o usuário digitar uma opção diferente das apresentadas no menu, exibir 'Opção inválida!!!'
# Exibir no final do processamento 'Fim do programa!'


print("Opção 1")
print("Opção 2")
print("Opção 3")
print("Sair")

o3 = input("Escolha uma opção: ")

if o3 == "Opção 1":
    print("Você selecionou a opção 1")
elif o3 == "Opção 2":
    print("Você selecionou a opção 2")    
elif o3 == "Opção 3":
    print("Você selecionou a opção 3")
elif o3 == "Sair":
    print("Você selecionou sair")  
else:
    print("Opção inválida!!!")

    print(f"Sua escolha foi: {o3}")
