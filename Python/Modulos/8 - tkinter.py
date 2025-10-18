import tkinter as tk

# 1 - Criando a Janela

window = tk.Tk()
window.geometry("450x300")
window.title("Gerencia Frases")

# 2 - Adicionando um Frame
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill="x", expand=True)

# 3 - Adicionando um Label
nome = input("Digite seu nome: ")
label = tk.Label(frame, text=(f"Olá {nome}, Seja Bem-Vindo!, O que deseja fazer?"))
label.pack(fill="x", expand=True)

window.mainloop()


# qual opcao necessaria para criar uma janela basica com o modulo tkinter?# R: A opção correta é utilizar a classe Tk() do módulo tkinter para criar uma janela básica
# root = tkinter.Tk() 
# windows = TkWindow() 
# # main_window = tkinter.Window() 