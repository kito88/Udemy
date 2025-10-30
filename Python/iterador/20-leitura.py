import xml.etree.ElementTree as ET

# Caminho do seu XML
arquivo = 'Nfe1.xml'

# Lê o arquivo
tree = ET.parse(arquivo)
root = tree.getroot()

# Detecta o namespace automaticamente
namespace = root.tag[root.tag.find("{")+1 : root.tag.find("}")]
ns = {'nfe': namespace}

# Percorre todas as tags e valores
for elem in root.findall('.//nfe:*', ns):
    tag = elem.tag.split('}')[-1]  # remove o namespace da tag
    valor = elem.text.strip() if elem.text else ''
    print(f"{tag}: {valor}")

# with open("Oi.doc", "r", encoding="utf-8") as arquivo:
#     print(arquivo.read())

# explica o que pode ser recuperado 

#with open("Oi.doc", "r", encoding="cp1252") as arquivo:
#    print(arquivo.read())




# with open("Oi.doc", "rb") as f:
#     result = chardet.detect(f.read())
#     print(result)
