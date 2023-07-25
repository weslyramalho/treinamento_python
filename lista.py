lista1=[] #inicializa lista vazia
lista2=[10,20,30]#lista com valor

print(lista2)

#adicionando elementos na lista 1 atraves do append() metodo
lista2.append(54)
print(lista2)

aux = lista2.pop()
print("Elemento removido:", aux)#remove o último elemento
print(lista2)

"""append() =>Metodo para adicionar um elemento no final da lista.
   pop => remove ultimo elemento da lista
"""