"""
* args - Utilizamos ele quando não temos certeza de quantos argumentos queremos para uma função.
- Os Argumentos são passados como uma tupla 
**kwargs- Além dos valores podemos também passar as respctivas chaves para cada Argunmento
- Os Argumentos são passados como um dicionário
"""

#1 - Soma de Números com o args
def sum(*num):
    sum_total = 0
    for n in num:
        sum_total += n
    print(f"Soma é: {sum_total}")


sum(7)
sum(7, 3)
sum(7, 3, 5)
sum(7, 3, 5, 8, 2, 1, 4)


# 2 - Apresentação de Cursos
def presentation(**data):
    for key, value in data.items():
        print(f"{key}: {value}")
print("Lista de Cursos")
presentation(name="Python", category="Backend", Level="Iniciante")
presentation(name="Visão Computacional", category="IA", Level="Avançado")
presentation(name="Dashborads com Dash", category="Data Science", Level="Intermediario")