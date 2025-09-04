movieName = "O Poderoso Chefão"
movieDescription = """
    O Poderoso Chefão é um filme de 1972
    dirigido por Francis Ford Coppola,
    baseado no romance de 1969 de Mario Puzo.
    Estrelado por Marlon Brando e Al Pacino,
"""

print(movieName.upper())  # Deixa todas as letras maiusculas
print(movieName.lower())  # Deixa todas as letras minusculas
print(movieName.capitalize())  # Deixa a primeira letra maiuscula
print(movieName.title())  # Deixa todas as palavras com a primeira letra maiuscula
print(movieName.center(50, '-'))  # Centraliza a string em um espaço de 50 caracteres
print(movieName.strip())  # Remove espaços no começo e no final
print(movieName.split())  # Transforma a string em uma lista
print("Poderoso" in movieName)  # Verifica se a palavra está na string
print("Poderoso" not in movieName)  # Verifica se a palavra não está na string
print(movieName.replace("o", "0"))  # Substitui uma palavra por outra
print(movieName.find("Chefão"))  # Retorna o indice da palavra
print(movieName.find("Inexistente"))  # Retorna -1 se a palavra não for encontrada
print(len(movieName))  # Retorna o tamanho da string
print(movieDescription)strip())  # Remove espaços no começo e no final
print(movieDescription.split())  # Transforma a string em uma lista
print("Francis" in movieDescription)  # Verifica se a palavra está na string
print("Francis" not in movieDescription)  # Verifica se a palavra não está na string

