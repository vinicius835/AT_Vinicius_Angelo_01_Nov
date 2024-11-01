import tkinter as tk
janela = tk.Tk()

var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mail proporcionais", variable=var_promocoes)
checkbox_promocoes.grid(row=0,column=0)
def enviar():
    print(var_promocoes.get())

botao_enviar = tk.Button (text="Enviar", command= enviar)
botao_enviar.grid(row= 1, column=0)

janela.mainloop()
