# #Informações sobre o Filme
# name = input("Digite o nome do Filme: \n")
# yearRelease = int(input("Digite o Ano de Lançamento do Filme: \n"))
# rating = float(input("Digite a Nota do Filme: \n"))

# #Verifica se o filme é recomendado
# if rating >= 7 and yearRelease >= 2015:
#     print(f"O filme {name} é muito bom, eu recomendado Assisti-lo!")
# else:
#     print(f"O filme {name} não é tão bom, você pode pular esse filme.")


#Outro Exemplo

num1 = int(input("Digite o primeiro numero: \n"))
num2 = int(input("Digite o segundo numero: \n"))
operation = input("Digite a operação (+, -, *, /): \n")

if operation == "+":
    result = num1 + num2
    print(f"O resultado de {num1} + {num2} é: {result}")    
elif operation == "-":
    result = num1 - num2
    print(f"O resultado de {num1} - {num2} é: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"O resultado de {num1} * {num2} é: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"O resultado de {num1} / {num2} é: {result}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")

print(f"O resultado da operação é: {result:.3f}")