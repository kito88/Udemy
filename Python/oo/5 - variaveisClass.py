<<<<<<< HEAD
    #metodos contructor
class Game:
    total_games = 0  # Variável de classe para contar o número total de jogos criados
    def __init__(self, name="", yearLaunch = 0, multiplayer = 0, note = 0):
        self.name = name # Variável de instância
        self.yearLaunch = yearLaunch # Variável de instância
        self.multiplayer = multiplayer # Variável de instância
        self.note = note # Variável de instância
        Game.total_games += 1  # Incrementa o contador de jogos toda vez que um novo jogo é criado
        self.totalEvaluation = 0 # Variável de instância para armazenar a soma das avaliações
        self.evaluators = 0 # Variável de instância para armazenar o número de avaliadores
=======
class Game:
    total_games = 0 # Variavel de Classe para contar o número total de Jogos!
    def __init__(self, name="", yearLaunch = 0, multiplayer = 0, note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
        Game.total_games += 1
        self.totalEvaluation = 0
        self.evaluators = 0
>>>>>>> 875adfd46ace8883a41b7f2e4c0a3d1a9408a9cd
    
    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        print("#### Dados do Jogo ####")
<<<<<<< HEAD
        print(f" Nome: {self.name} ")
        print(f" Ano de Lançamento: {self.yearLaunch}")
        print(f" Multiplayer: {self.multiplayer} ")
        print(f" Nota: {self.note} \n")

game1 = Game("God of War", 2018, False, 9.5)
game2 = Game("Fifa 21", 2020, True, 9.8)

print("Dados do Jogo")
print(f"\n Nome: {game1.name} - Anos de Lançamento: {game1.yearLaunch} - Multiplayer: {game1.multiplayer} - Nota: {game1.note}") 
print(f"\n Nome: {game2.name} - Anos de Lançamento: {game2.yearLaunch} - Multiplayer: {game2.multiplayer} - Nota: {game2.note}")


game1.technical_sheet()
game2.technical_sheet()
print(game1)
=======
        print(f" Nome do Jogo: {self.name} ")
        print(f" Ano de Lançamento: {self.yearLaunch}")
        print(f" Multiplayer: {self.multiplayer} ")
        print(f"Total de Avaliações é : {self.note}\n")


    def evaluate (self, note):
        self.totalEvaluation =+ note
        self.evaluators =+ 1

    def average(self):
        print(f"Media do Jogo {self.name} : {self.totalEvaluation / self.evaluators}")
        
game1 = Game("God of War", 2018, False, 9.5)
game2 = Game("Fifa 21", 2020, True, 9.8)
game3 = Game("Mario Bros", 2025, True, 10.0)

game1.technical_sheet()
game2.technical_sheet()
game1.evaluate(9.7)
game1.evaluate(8.8)
game2.evaluate(7.9)
game2.evaluate(10.0)
game1.average()
game2.average()


#Exibindo a qtde de Jogos Criado
print(f"Total de Jogos criados: {Game.total_games }")
>>>>>>> 875adfd46ace8883a41b7f2e4c0a3d1a9408a9cd
