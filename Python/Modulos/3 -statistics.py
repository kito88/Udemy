# Modulo referente as Statisticas Nativo de python

import statistics

# 1 - calcular a média de uma lista de números
data = [10, 20, 30, 40, 50]
mean = statistics.mean(data)
print(f"Média: {mean}")

# 2 - calcular a mediana de uma lista de números
median = statistics.median(data)
print(f"Mediana: {median}")

# 3 - Aplicando a Moda
data_with_mode = [10, 20, 20, 30, 40, 50]
mode = statistics.mode(data_with_mode)
print(f"Moda: {mode}")

# 4 - Desvio Padrão
"""
Quanto Mais Proximo de 0 for o Desvio Padrão, Significa que os dados do conjunto estão menos dispersos"""
std_dev = statistics.stdev(data)
print(f"Desvio Padrão: {std_dev:.2f}")
