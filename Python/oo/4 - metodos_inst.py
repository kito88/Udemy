#metodos contructor
class Game:
    def __init__(self, name="", yearLaunch = 0, multiplayer = 0, note = 0):
        self.name = name
        self.yearLaunch = yearLaunch
        self.multiplayer = multiplayer
        self.note = note
    
    def __str__(self):
        return f"Game: {self.name}"

    def technical_sheet(self):
        print("#### Dados do Jogo ####")
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