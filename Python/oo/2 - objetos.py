class Game:
    name = ""
    yearLaunch = 0
    multiplayer = False
    note = 0

#1 - Primeiro Jogo
game1 = Game()
game1.name = "The Last of Us Part II"
game1.yearLaunch = 2020
game1.multiplayer = False
game1.note = 9.5

# Segundo Jogo
game2 = Game() 
game2.name = "Fifa 23"
game2.yearLaunch = 2025
game2.multiplayer = True
game2.note = 9.8

print("Dados do Jogo")
print(f"\n Nome: {game1.name} - Anos de Lançamento: {game1.yearLaunch} - Multiplayer: {game1.multiplayer} - Nota: {game1.note}") 
print(f"\n Nome: {game2.name} - Anos de Lançamento: {game2.yearLaunch} - Multiplayer: {game2.multiplayer} - Nota: {game2.note}")
