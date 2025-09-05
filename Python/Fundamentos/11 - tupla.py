filmsTuple = ("Inception", "The Shawshank Redemption",
              "The Dark Knight","Pulp Fiction","InterStellar")
print(type(filmsTuple)) # <class 'tuple'>

# 1 - Buscar os dois Primeiros Itens da Tupla
print(filmsTuple[:2]) # ('Inception', 'The Shawshank Redemption')

# 2 - Buscar o ultimo Item da Tupla
print(filmsTuple[-1]) # InterStellar

# 3 - Buscar Item até uma determinada posição
print(filmsTuple[:3]) # ('Inception', 'The Shawshank Redemption', 'The Dark Knight')
# ou print(filmList[0:3])

#4 - Buscar um Item de uma determinada posição em Diante
print(filmsTuple[1:4]) # ('The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction')

# 5 - Recupera Item da Tupla pelo nome
print(filmsTuple.index("InterStellar")) # 4

