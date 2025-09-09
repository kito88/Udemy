"""#lista de Filmes
movieList = ["titanic", "avatar", "star wars", "matrix", "interestelar"]

# 1 - iterando valores de uma lista de filmes usando While
index = 0
while index < len(movieList):
    print(movieList[index])
    index += 1

# 2 - Quando uma iteração for atendida o Loop será encerrado
index = 0
while index < len(movieList):
    if movieList[index] == "matrix":
        break
    print(movieList[index])
    index += 1

# 3 - Quando uma iteração for atendida o Loop Irá pular para a próxima iteração
index = 0
while index < len(movieList):
    if movieList[index] == "matrix":
        index += 1
        continue
    print(movieList[index])
    index += 1

# 4 - Avaliação do Filme com While
movieName = input("Digite o nome do Filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))
total = 0
count = 0

while count < movieRating:
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    count += 1

    
if movieRating > 0:
    average = total / movieRating
else:
    average = 0


print(f"Média de Avaliação do Filme {movieName} é: {average:.2f}")

"""
