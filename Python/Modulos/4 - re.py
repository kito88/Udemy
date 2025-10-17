# - Modulo REGEX
import re

# 1 - Indice Inicial e Final de Palavras
# o r significa uma row string(string Bruta)
text = "Udemy - Uma Plataforma de Cursos Online"
match = re.search(r'de Cursos', text)
print(f"Indice Inicial: {match.start()}")
print(f"Indice Final: {match.end()}")

# 2 - Buscando o indice que possui o Ponto
site = "www.udemy.com"
match = re.search(r'\.', site)
print(f"Indice do Ponto: {match.start()}")

# 3 - Buscando uma lista de caracteres dentro de uma Frase
phrase = "Ola, meu nome é João e tenho 30 anos"
match = re.findall(r'[aeiou]', phrase) # lista de vogais    
print(f"Vogais Encontradas: {match}")

#Metodo Do Professor
pattern = "[a-m]"
result = re.findall(pattern, text)
print(result)

# 4 - Verificando o inicio de uma String
rule = r"A"
phrases = ["A casa está Suja", "O Dia esta Lindo", "Vamos Passear"]
for i in phrases:
    if re.match(rule, i):
        print(f"A frase '{i}' começa com A")
    else:
        print(f"A frase '{i}' não começa com A")

# 5 - Verificando o fim de uma String
rule_end = r"o$"
phrases2 = ["Ola Mundo", "Ola Pessoal", "Vamos ao Cinema com Amigo"]
print(phrases2)
for f in phrases2:    
    match = re.search(rule_end, f)
    if match:
        print(f"A frase '{f}' termina com 'o'")
    else:
        print(f"A frase '{f}' não termina com 'o'")
        