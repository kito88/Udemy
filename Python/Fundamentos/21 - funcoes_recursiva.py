""""
    Fatorial de um Numero:
    1 -> 1 * 1
    2 -> 2 * 1 
    3 -> 3 * 2  * 1
"""

# 1 - Fatorial de um Número
def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

number = int(input("Digite o número para o fatorial: \n"))
print(f"O Fatorial de {number} é {factorial(number)}")

# 2 - a Soma total de um número
def num_soma(num):
    if num == 1:
        return 1
    else:
        return (num + num_soma(num - 1))
    
num = int(input("Digite o número para a Soma: \n"))
print(f"a Soma Total de {num} é {num_soma(num)}")

# revendo valores a ser Seguidos