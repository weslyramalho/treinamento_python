produto = {
    'codigo': 0,
    'descricao': "",
    'preco': 0.0,
    'qtde': 0.0
}

produto['codigo'] = int(input("Digite o código do produto: \n"))
produto['descricao'] = input("Digite a descrição do produto:\n")
produto['preco'] = float(input("Digite o preço unitário do produto: \n"))
produto['qtde'] = float(input("Digite a quantidade em estoque: \n"))

print("Código: ", produto['codigo'])
print("Descrição:", produto['descricao'])
print("Preço Unitário R$ {:.2f}".format(produto['preco']))
print("Quantidade em Estoque", produto['qtde'], "\n")


                             