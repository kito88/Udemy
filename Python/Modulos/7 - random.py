import random

print(random.random())  # Gera um número float aleatório entre 0.0 e 1.0
print(random.randint(1, 10))  # Gera um número inteiro aleatório entre 1 e 10 (inclusive)
print(random.choice(['apple', 'banana', 'cherry']))  # Escolhe aleatoriamente um item de uma lista
print(random.sample(range(60), 6))  # Seleciona 5 números únicos

# Embaralha uma lista
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# programa adivinhe o Numero 
secret = False
while not secret:
    print(" O que Deseja Fazer?")
    print("1 - Jogar!")
    print("2 - Sair")

    choice = input(">")
    if choice == "1":
        print("===============Advinhe o Número de 1 a 10 ==================")
        number = int(input("Digite um Número de a 10:\n"))
        result = random.randint(1, 10)
        if number == result:
            print("Parabéns Você Acertou")
        else:
            print(f"Tente Novamente, o Número Sorteado foi {result}")
    elif choice == "2":
        secret = True
        print("Saindo do Jogo....")
    else:
        print("Opção Inválida, Tente Novamente")