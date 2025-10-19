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
        
# Classe Derivada (Subclasse) -Especializada
class singlePlayerGame(Game):
    def __init__(self, name="", yearLaunch = 0, note = 0, storyline = 0):
        super().__init__(name, yearLaunch, multiplayer = False, note = note)
        self.storyline = storyline

    def technical_sheet(self):
        super().technical_sheet()
        print(f"Enredo: {self.storyline}\n")

multigame = Game("Fortnite", 2018, True, 8.3)
multigame.technical_sheet()

sing_game = singlePlayerGame("Mario Bros", 2026, 10, "Emocionante Jogo de Aventura que tem como Objetivo Salvar uma Princesa!")
sing_game.technical_sheet()

sing_game = singlePlayerGame("Corrida Maluca", 2012, 8, "Corrida Maluca são formadas por 8 carros malucos que tentam pegar um Pombo")
sing_game.technical_sheet()
