#lista de Filmes
movieList = ["titanic", "avatar", "star wars", "matrix", "interestelar"]

#iterando valores da uma lista
for movie in movieList:
    print(movie)

print("~~~" * 25 )

#iterando valores da uma lista com indice
for movie in movieList:
    if movie == "matrix":
        continue
    print(f"{movie}")

# 4 - Avaliação do Filme
movieName = input("Digite o nome do Filme: \n")
movieRating = int(input("Digite quantas avaliações deseja fazer: \n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme: \n"))
    total += note
    print(total)
if movieRating > 0:
    average = total / movieRating
else:
    average = 0 

print(f"A média das avaliações para o filme {movieName} é: {average:.2f}") 
