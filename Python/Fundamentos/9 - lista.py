filmMatrix = ["Matrix, 1999, 8.7, True"]
print(filmMatrix)

filmList = ["Inception","The Shawshank Redemption",
            "The Dark Knight","Pulp Fiction","InterStellar"]

# 1 -  Buscar os dois Primeiros Itens da Lista
print(filmList[:2])

# 2 - Buscar o ultimo Item da Lista
print(filmList[-1])

# 3 - Buscar Item até uma determinada posição
print(filmList[:3]) # ou print(filmList[0:3])

# 4 - Buscar Item a partir de uma determinada posição
print(filmList[1:4]) # ou print(filmList[1:]) com ambos os codigos irá retornar os itens 1,2 e 3

# 5 - Buscar Item de trás para frente
print(filmList[::-1]) # ou print(filmList[-1:-6:-1) com ambos os codigos irá retornar todos os itens da lista de tras para frente