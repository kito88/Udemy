movieName = "Top Gun"

#string[inicio:fim] - Indice começa na posição 0 / indice final - 1

# 1 - Buscar toda string a partir da primeiro posição

print(movieName[0:]) # "Top Gun"
print(movieName[:4]) # "Top"

#2 - Buscar toda string a partir da Terceira posição
print(movieName[2:]) # "p Gun"

# 3 - Buscar toda string a partir da segunda posição até a quarta
print(movieName[1:4]) # "op "

# 4 - Buscar toda string a partir da segunda posição até a penultima posição
print(movieName[1:-1]) # "op Gu"

# 5 - Contar de trás para frente
print(movieName[::-1]) # "nuG poT"


"""
string[inicio:fim:passo] - Indice começa na posição 0 / indice final - 1 / passo - de quanto em quanto ele vai pular
"""
print(movieName[0::1]) # "Top Gun"
print(movieName[0::2]) # "TpGu" #Pula de 2 em 2
print(movieName[0::3]) # "T u" #Pula de 3 em 3    

# Buscar pelo Indices impares

print(movieName[1::2]) # "o n" #Pula de 2 em 2

# 6 