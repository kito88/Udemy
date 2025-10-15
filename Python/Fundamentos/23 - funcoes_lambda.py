# 1 - funcoes de potencia de um número
power = lambda num : num **2
print(power(5))
print(power(9))

#2 - funcao que verifique se o número é Par
is_even = lambda num: num % 2 == 0
print(is_even(4))  

# 3 - função que divide um número por outro.
div_num = lambda x,y: x / y 
print(div_num(10,2))
print(div_num(15,3))


# 4 - função que inverte uma strings
invert_str = lambda s: s[::-1]
print(invert_str("Python")) 
print(invert_str("JavaScript"))

# 5 - Funcionalidades Relacionais aos Filmes:
movie_list = ["Titanic", "The Godfather", "Inception", "Jurassic Park", "The Matrix"]
ratings = {
    "Titanic": [7.8, 9.0, 8,7]
    ,"The Godfather": [9.2, 9.5, 9.0]
    ,"Inception": [8.8, 9.0, 8.5]
    ,"Jurassic Park": [8.1, 8.5, 8.0]
    ,"The Matrix": [8.7, 9.0, 8.5]
}

# 6 - Função para calcular a media de Avaliação de um Filme
average_ratings = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])
print(f"Média de Avaliação do Filme Titanic: {average_ratings('Titanic')}")

# 7 - Função que verifica se um Filmes está na Lista
check_movie = lambda movie_name: movie_name in movie_list

print(f"O Filme Inception está na lista? {check_movie('Inception')}")
print(f"O Filme Avatar está na lista? {check_movie('Avatar')}")
# 8 - Função que adiciona um novo filme na lista
add_movie = lambda movie_name: movie_list.append(movie_name) if movie_name not in movie_list else f"O Filme {movie_name} já está na lista."
print(add_movie("Avatar"))
print(movie_list)
print(add_movie("Inception"))

# 9 -Função que recomenda um filme com base na avaliação média
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name}" if average_ratings(movie_name) >= 8.5 else f"{movie_name} não é altamente recomendado."
print(recommend_movie("The Godfather")) 
