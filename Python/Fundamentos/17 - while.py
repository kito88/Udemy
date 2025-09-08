#Lista de Filmes
movieList =  ["Titanic","The Godfather","Inception","Jurassic Park", "Velozes e Furiozos"]

# 1 - Iterando valores de uma Lista de Filmes usando While
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1

line = "~~"*20
print(line)

# 2 - Quando a condição for atentida o Loop será encerrado
index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        index += 1
        break;
    print(movieList[index])
    index += 1


line = "~~"*20
print(line)

# 3 - Quando a condição for atendida, o loop pulara e continua o bloco de codigo

index = 0
while index < len(movieList):
    if movieList[index] == "Inception":
        index += 1
        continue;
    print(movieList[index])
    index +=1