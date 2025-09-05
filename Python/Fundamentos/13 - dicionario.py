filmInception = {
    "title": "Inception",
    "year": 2010,
    "imdbRating": 8.8,
    "genre": ["Action", "Adventure", "Sci-Fi"],}

# 1 = Recuperar um elemento do Dicionario
print(filmInception)
print(len(filmInception)) # 4
print(type(filmInception))# <class 'dict'>
print(filmInception["title"]) # Inception

# 2 - Buscar Apenas as Chaves do Dicionario
print(filmInception.keys()) # dict_keys(['title', 'year', 'imdbRating', 'genre'])

#3 - Buscar apenas os Valores do Dicionario
print(filmInception.values()) # dict_values(['Inception', 2010, 8.8, ['Action', 'Adventure', 'Sci-Fi']])

#4 - Buscar Itens do Dicionario com chave e Valor
print(filmInception.items()) # dict_items([('title', 'Inception'), ('year', 2010), ('imdbRating', 8.8), ('genre', ['Action', 'Adventure', 'Sci-Fi'])]

#5 - Adicionar um Item no Dicionario)
filmInception["director"] = "Christopher Nolan" # Adiciona o item no dicionario
print(filmInception)

#6 - Remover um Item do Dicionario
filmInception.pop("imdbRating") # Remove o item do dicionario

# 7 - Atualizar itens do Dicionario
filmInception.update({"imdbRating": 8.2}) # Atualiza o item do dicionario
print(filmInception)