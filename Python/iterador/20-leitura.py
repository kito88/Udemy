
import chardet

# with open("Oi.doc", "r", encoding="utf-8") as arquivo:
#     print(arquivo.read())

#with open("Oi.doc", "r", encoding="cp1252") as arquivo:
#    print(arquivo.read())




with open("Oi.doc", "rb") as f:
    result = chardet.detect(f.read())
    print(result)
