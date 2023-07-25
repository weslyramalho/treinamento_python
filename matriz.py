mat = []
"""
mat.append([1,2,3])
mat.append([4,5,6])
mat.append([7,8,9])

"""

for i in range(3):
    linha=[]
    for j in range(3):
        dado = int(input("Digite um valor: "))
        linha.append(dado)
    mat.append(linha)

for i in range(3):
    for j in range(3):
        print("elemento da linha ", i , "e coluna ", j , "e: ", mat[i][j])