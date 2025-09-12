# - Função para imprimir uma Mensagem.
def printMessage():
    print("Olá Mundo!")

printMessage()

#2 - Função para Calcular a Média de um Filme
def calculateAverage():
    num_Ratings = int(input("Digite quantas avaliações deseja fazer: \n"))
    total = 0
    for i in range(num_Ratings):
        note = float(input("Digite a nota para o filme: \n"))
        total += note
    if num_Ratings > 0:
        average = total / num_Ratings
    else:
        average = 0

    return average

print(f"Média de Avaliação do Filme é: {calculateAverage():.2f}")