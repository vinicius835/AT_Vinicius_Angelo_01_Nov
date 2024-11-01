import tkinter as tk
janela = tk.Tk()
var_promocoes = tk.IntVar()
checkbox_promocoes = tk.Checkbutton(text="Deseja receber e-mail promocional?",variable=var_promocoes)
checkbox_promocoes.grid(row=0,column=0)

var_politica = tk.IntVar()
checkbox_politica = tk.Checkbutton(text="Aceitar termos de Uso e Políticas de Privacidade",variable=var_politica)
checkbox_politica.grid(row=1,column=0)
def enviar():
    if var_promocoes.get():
        print("Usuário deseja receber promoções")
    else:
        print("Usuário não deseja receber promoções")
    if var_politica.get():
        print("Usuário concordou com Termos de Uso e Politicas de Privacidade")
    else:
        print("Usuário não concordou com Termos de Uso e Politicas de Privacidade")
botao_enviar = tk.Button(text="enviar",command=enviar)
botao_enviar.grid(row=2,column=0)
janela.mainloop()
