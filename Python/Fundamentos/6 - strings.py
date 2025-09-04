movieName = "Top Gun"
movieName2 = "top Gun"
print(movieName == movieName2)  # False #Case Sensitive
print(movieName.lower() == movieName2.lower())  # True

movieDescription = """
    Top Gun é um filme de ação americano de 1986, 
    dirigido por Tony Scott, com roteiro de Jim Cash e Jack Epps Jr., 
    estrelado por Tom Cruise como o personagem-título.
"""

print(movieName)
line = "---"
print(line*30)
print(movieDescription)

print("top" in movieName)  # False
print("Top" in movieName) # True    