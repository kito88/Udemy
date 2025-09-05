filmList = ["Inception","The Shawshank Redemption",
            "The Dark Knight","Pulp Fiction","InterStellar"]

# 1 - Verificar o Tamanho da Lista
print(f"está é quantidade de Item da Lista: {len(filmList)}") # ou print(len(filmList)) # Retorna a quantidade de itens da lista    

# 2 - Recuperar um Item da Lista pelo Nome
print(f" em Qual Posição está o Item Referente ao 'InsterStellar': {filmList.index("InterStellar")}") # ou print(filmList.index("InterStellar")) # Retorna o indice do item

# 3 - Adicionar um Item no Final da Lista
filmList.append("The Matrix") # Adiciona o item no final da lista
print(filmList)

# 4 - Ordenar a Lista
filmList.sort() # Ordena a lista em ordem alfabetica
print(filmList)

# 5 - Copiar todos os Itens da Lista para Outra e Excluir um Item pelo Nome
filmsCopy = filmList.copy() # ou filmsCopy = filmList[:] ambos os codigos irão copiar todos os itens da lista
filmsCopy.remove("The Shawshank Redemption")
print(filmsCopy)

# 6 - Remover Todos os Itens da Lista
filmsCopy.clear() # Remove todos os itens da lista
print(filmsCopy)