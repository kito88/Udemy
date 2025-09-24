# 1 - Função para imprime um nome Completo
def fullName(firstName, LastName):
    print(f"Nome é: {firstName} {LastName}")

fullName("Arthur","Gonçalves")
fullName("Maria","Silva")

# 2 - Função para somar dois Numeros:
def sumNumbers(a, b):
    return a + b
print(f"A Soma é: {sumNumbers(5, 10)}")
print(f"A Soma é: {sumNumbers(15, 25)}")


# 3 - Função com parametros Default
def adress(country="Brasil"):
    print(f"Eu moro em: {country}")

adress()
adress("Argentina")
# 4 - Função para Avaliar um Filme
filme = input("Digite o nome do Filme: \n")
def rateMovie(movieName, num_Ratings):
    total = 0
    for i in range(num_Ratings):
        note = float(input(f"Digite a nota para o filme {movieName}: \n"))
        total += note
    if num_Ratings > 0:
        average = total / num_Ratings
    else:
        average = 0
    
    print(f"Média de Avaliação do Filme {movieName} é: {average:.2f}")
rateMovie(filme, 0) # chamando a função rateMovie com os parametros do Nome do Filme e mais a quantidade de avaliações do determinado Filme