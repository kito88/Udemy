name = input("Digite o Nome do Filme:\n")
yaerLaunch = int(input("Digite o Ano de Lançamento do Filme:\n"))
noteMovie = float(input("Digite a Nota do Filme:\n"))

print(name)
print(yaerLaunch)
print(noteMovie)

print("Dados do filme")
print("========================================")
print(name, "foi lançado em: ", yaerLaunch, "e sua nota é: ", noteMovie)

print(f"Dados do filme: {name} foi lançado em: {yaerLaunch} e sua nota é: {noteMovie}")