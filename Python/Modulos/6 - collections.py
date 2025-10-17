from collections import Counter, defaultdict, namedtuple, deque
from operator import itemgetter

fruits = ["maçã", "banana", "laranja", "maçã", "banana", "maçã","uva","Abacaxi","banana", "Melância", "Melancia", "Melão", " Melão", "Banana", "Maçã"]
fruits = [item.capitalize().strip() for item in fruits]  # Normalizando os nomes das frutas
# 1 - Contar a frequência de elementos em uma lista
fruit_counter = Counter(fruits)
print(f"Frequência de frutas: {fruit_counter}")

print("=="*20)

# 2 - Utilizando defaultdict para agrupar frutas por sua primeira letra
fruit_dict = defaultdict(list)
for fruit in fruits:
    first_letter = fruit[0].upper()  # Convertendo para maiúscula para evitar duplicatas
    fruit_dict[first_letter].append(fruit)
print(f"Frutas agrupadas por letra inicial: {dict(fruit_dict)}")

print("=="*20)

# 3 - Utilizando namedtuple para representar uma fruta com nome e quantidade
Fruit = namedtuple('Fruit', ['name', 'quantity', 'price'])
apple = Fruit(name='Maçã', quantity=10, price=2.5)
banana = Fruit(name='Banana', quantity=5, price=3.0)
print(f"Fruta: {apple.name}, Quantidade: {apple.quantity}, Preço: {apple.price}")
print(f"Fruta: {banana.name}, Quantidade: {banana.quantity}, Preço: {banana.price}")

print("=="*20)

# 4 - Utilizando deque para uma fila de frutas
fruit_queue = deque(fruits)
fruit_queue.append("Manga")
print(f"Fila de frutas após adicionar Manga: {fruit_queue}")
fruit_queue.popleft()
print(f"Fila de frutas após remover a primeira fruta: {fruit_queue}")

print("=="*20)

# 5 - Ordenando frutas por frequência usando itemgetter
sorted_fruits = sorted(fruit_counter.items(), key=itemgetter(1), reverse=True)
print(f"Frutas ordenadas por frequência: {sorted_fruits}")

print("=="*20)

# 6 - Encontrando as 3 frutas mais comuns
most_common_fruits = fruit_counter.most_common(3)
print(f"As 3 frutas mais comuns: {most_common_fruits}")

print("=="*20)

# 7 - Limpando a contagem de frutas
fruit_counter.clear()
print(f"Contagem de frutas após limpar: {fruit_counter}")

