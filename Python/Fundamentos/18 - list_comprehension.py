# 1 - listando valores de 0 a 10 que seja menor do que 4
listNumbers = [x for x in range(10) if x < 4]
print(listNumbers)

# Lista de Filmes
movieList = ["titanic", "avatar", "star wars", "matrix", "interestelar"]

# 2 - Filmes que começam com a letra "s"
listMoviesS = [movie for movie in movieList if 's' in movie.lower()]
print(listMoviesS)


# 3 - Filmes que ja assitir
watchedMovies = ["titanic", "matrix"]
listWatchedMovies = [movie for movie in movieList if movie != "matrix"]
print(listWatchedMovies)

# 4 - Encontrrando um Filme pelo Nome:
cor_negrito = "\033[1;30m"
cor_reset = "\033[0m"
cor_italico = "\033[3;30m"
while True:
    searchName = input("Digite o nome do Filme que deseja pesquisar ou 'sair' para encerrar: \n")
    if searchName.lower() == 'sair':
        print("Programa Encerrado!")
        break

    foundMovies = [movie for movie in movieList if searchName.lower() in movie.lower()]
    if foundMovies:
        print(f"Filme(s) Encontrado(s): {cor_negrito}{searchName} {cor_reset}:")
        for foundMovie in foundMovies:
            print(foundMovie)
    else:
        print(f"Nenhum Filme Encontrado com o Nome:{cor_negrito} {cor_italico}{searchName}. {cor_reset} {cor_italico} Tente Novamente.{cor_reset}")




searchMovie = input("Digite o nome do Filme que deseja pesquisar: \n")
foundMovies = [movie for movie in movieList if searchMovie.lower() in movie.lower()]
print(foundMovies)