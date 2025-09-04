num1 = int(input("Digite o Primeiro número:\n"))
num2 = int(input("Digite o Segundo número:\n"))

#Aritméticos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2
exponenciacao = num1 ** num2
modulo = num1 % num2
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão Inteira: {divisao_inteira}")
print(f"Exponenciação: {exponenciacao}")
print(f"Módulo: {modulo}")
#Atribuição
num1 += 10 #num1 = num1 + 10
print(num1)
num1 -= 10 #num1 = num1 - 10
print(num1)
num1 *= 10 #num1 = num1 * 10
print(num1)
num1 /= 10 #num1 = num1 / 10
print(num1)
num1 //= 10 #num1 = num1 // 10
print(num1)
num1 **= 10 #num1 = num1 ** 10
print(num1)
num1 %= 10 #num1 = num1 % 10
print(num1)
print(type(num1))
#Comparação
print(num1 == num2) #Igual
print(num1 != num2) #Diferente
print(num1 > num2)  #Maior
print(num1 < num2)  #Menor
print(num1 >= num2) #Maior ou Igual
print(num1 <= num2) #Menor ou Igual
#Lógicos
print(num1 > 5 and num2 < 10) #E
print(num1 > 5 or num2 < 10)  #Ou
print(not(num1 > 5 or num2 < 10)) #Negação
#Identidade
print(num1 is num2) #É o mesmo objeto?
print(num1 is not num2) #Não é o mesmo objeto?
#Pertinência
lista = [1,2,3,4,5]
print(num1 in lista) #Está na lista?
print(num1 not in lista) #Não está na lista?
print(type(lista))
#Prioridade de operadores
print(5 + 3 * 2) #Multiplicação antes da soma
print((5 + 3) * 2) #Parênteses antes da multiplicação
print(5 + 3 * 2 ** 2) #Exponenciação antes da multiplicação
print((5 + 3) * 2 ** 2) #Parênteses antes da exponenciação
print((5 + 3 * 2) ** 2) #Parênteses antes da exponenciação
print(((5 + 3) * 2) ** 2) #Parênteses antes da exponenciação
#Comentários
#Isso é um comentário
"""Isso é um comentário
de múltiplas linhas"""      
#Documentação
"""
Isso é um comentário
de múltiplas linhas de documentação
"""
#Docstring
def funcao():
    """
    Isso é um comentário
    de múltiplas linhas de documentação
    de uma função
    """
    return None