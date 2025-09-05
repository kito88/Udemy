filmsSet = {"Inception", "The Shawshank Redemption",
              "The Dark Knight","Pulp Fiction","InterStellar"}
print(type(filmsSet)) # <class 'set'>

# 1 - Buscar o Tamanho do Set
print(len(filmsSet)) # 5

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Inception", True, 1, 8.7}

# 3 - Adicionar Item de outro Set
filmsSet.update(exampleSet) # Adiciona todos os itens do outro set
print(filmsSet)

# 4 - Remver um Item do Set
filmsSet.remove("Pulp Fiction") # Remove o item do set
filmsSet.remove("InterStellar") # Remove o item do set
print(filmsSet) 