import pprint

filmsDict = {
    "Inception":{
        "yearLaunch": 2010,
        "imdbRating": 8.3,
        "genre": ["Action", "Adventure", "Sci-Fi"]
    },
    "InterStellar":{
        "yearLaunch": 2014,
        "imdbRating": 8.9,
        "genre": ["Adventure", "Drama", "Sexo"]  
    },
    "The Dark Knight":{
        "yearLaunch": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Crime", "Drama"]
    },
}
pp = pprint.PrettyPrinter(depth=4)  
pp.pprint(filmsDict) 
line = "-" * 50
print(line)

# 1 - Recuperar um elemento do Dicionario

print(filmsDict["Inception"]) # {'yearLaunch': 2010, '

print(filmsDict["The Dark Knight"]["imdbRating"]) # 9.0 
print(f"O Generos são : {filmsDict["Inception"]["genre"]}") 
print(line)

# 2 = Adicionar um Item no Dicionario
filmsDict["The Matrix"] = {
    "yearLaunch": 1999,
    "imdbRating": 8.7,
    "genre": ["Action", "Sci-Fi"]
}   
filmsDict["The Dark Knight"]["Personagem"] = "Batman e Coringa"
filmsDict["Inception"]["Director"] = "Christopher Nolan" # Adiciona o item no dicionario
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 3 - Excluir um item do Dicionario
filmsDict.pop("InterStellar") # Remove o item do dicionario
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)
print(line)


"""
    modelo de uma lista
    variavel = [] = é colchetes

    modelo de uma tupla
    variavel = () = é parenteses

    modelo de um set
    variavel = {} = é chaves

    modelo de um dicionario
    variavel = {"chave": "valor"} = é chaves, porém com chave e valor


"""

