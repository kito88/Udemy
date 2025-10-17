import hashlib
"""
Modulo Hashlib - Utilizado para criar um hash de uma string
Hash - Uma função que transforma uma string de qualquer tamanho em uma string de tamanho fixo

"""

# 1 - Verificar os algoritmos disponiveis
print(hashlib.algorithms_available) #

# 2 - Utilizando o Algoritmos  de acordo com o SO
print(hashlib.algorithms_guaranteed) # Algoritmos garantidos

# 3 - Utilizando o SHA 256
algorithm =hashlib.sha256()
print(algorithm.digest())
message = "A Melhor forma de prever o Futuro é Cria-lo".encode() # encode - transforma a string em bytes
algorithm.update(message)
print(algorithm.hexdigest())

# Outra forma de utilizar o SHA256
hash = hashlib.sha256()
hash.update(b"Senha1234") # b - string em bytes
print(f"SHA256: {hash.hexdigest()}")

# 4 - Utilizando o MD5
hash_md5 = hashlib.md5()
hash_md5.update(b"Senha1234")
print(f"MD5: {hash_md5.hexdigest()}")