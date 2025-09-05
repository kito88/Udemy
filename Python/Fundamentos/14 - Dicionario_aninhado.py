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
    }
}
pp = pprint.PrettyPrinter(depth=4)  
pp.pprint(filmsDict) 

# 1 - Recuperar um elemento do Dicionario
print(filmsDict["Inception"]["genre"]) # ['Action', 'Adventure', 'Sci-Fi']

# 2 = Adicionar um Item no Dicionario
filmsDict["The Matrix"] = {
    "yearLaunch": 1999,
    "imdbRating": 8.7,
    "genre": ["Action", "Sci-Fi"]
}   
filmsDict["Inception"]["Director"] = "Christopher Nolan" # Adiciona o item no dicionario
print(filmsDict["Inception"])


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

