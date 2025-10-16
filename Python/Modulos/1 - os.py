import os

# 1 - Retornar a Pasta Atual
print(os.getcwd())

# 2 - Listar arquivos e pastas
print(os.listdir())

# 3 - versão do Sistema Operacional
os.system('ver')

# 4 - Configuração da Maquina
#os.system('systeminfo')

# 5 - Limpar a Tela
os.system('cls')

# 6 - Exibir a Hora e Data da Maquina
os.system('echo %time%')
os.system('date /t')
os.system('echo %time%')
os.system('echo %date%')

# 7 - enviar email smtp