nome = input("Digite seu nome: \n")
sobrenome = input("Digite seu sobrenome: \n")

tamanho = len(nome) #retorna comrpimento do nome
print ("O tamanho de", nome, "é:", tamanho )

nome_completo= nome + " " + sobrenome
print("apos concatenar as strings temos: ", nome_completo)

if sobrenome in nome:
    print("o sobrenome", sobrenome, "está contido no nome", nome, ".")
print("O nome completo em minusculo é: ", nome_completo.lower())
print("O nome completo em maiusculo é: ", nome_completo.upper())