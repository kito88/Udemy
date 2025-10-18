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
    
    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        print("#### Dados do Jogo ####")
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