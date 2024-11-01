import tkinter as Tk
from tkinter import ttk
janela = Tk.Tk()
janela.title("Teste Titulo")
janela.rowconfigure(0,weight=1)
janela.columnconfigure(0,weight=1)
mensagem = Tk.Label(text="Sistema de busca de Cotação de moedas", fg="white", bg="#000000")
mensagem.grid(row=0,column=0,columnspan=2,sticky="NSEW")
mensagem2 = Tk.Label(text= "Selecione a moeda desejada")
mensagem2.grid(row=1,column=0)

mensagem3 = Tk.Label(text="Caso voce queira pagar mais de 1 cotação ao mesmo tempo, digite uma moeda a cada linha")
mensagem3.grid (row=4,column=0,columnspan=2)
caixa_texto = Tk.Text(width=10,height=5)
caixa_texto.grid(row=5,column=0,sticky="NSWE")



dicionario_cotacoes = {
    "dolar": 5.47,
    "euro": 6.68,
    "bitcoin":20000,
}

# moeda = Tk.Entry()
# moeda.grid(row=1,column=1)
moedas = list(dicionario_cotacoes.keys())
moeda = ttk.Combobox(janela,values = moedas)
moeda.grid(row=1,column=1)
def buscar_cotacao():
    moeda_preenchida = moeda.get()
    cotacao_moeda = dicionario_cotacoes.get(moeda_preenchida)
    mensagem_cotacao = Tk.Label(text= "Cotação não encontrada")
    mensagem_cotacao.grid(row= 3, column=0)
    if cotacao_moeda:
        mensagem_cotacao['text'] = f'cotação do {moeda_preenchida} é de {cotacao_moeda} reais'
botao = Tk.Button(text="Buscar Cotação",command=buscar_cotacao)
botao.grid(row= 2, column= 1)

def buscar_cotacoes():
    texto = caixa_texto.get("1.0",Tk.END)
    lista_moedas = texto.split("\n")
    # print(lista_moedas)
    mensagem_cotacoes = []
    for item in lista_moedas:
        cotacao =dicionario_cotacoes.get(item)
        if cotacao:
            mensagem_cotacoes.append(f'{item}:{cotacao}')
    mensagem4 = Tk.Label(text='\n'.join(mensagem_cotacoes))
    mensagem4.grid(row=6,column=1)
botao_multicotacoes = Tk.Button(text="Buscar Cotações",command=buscar_cotacoes)
botao_multicotacoes.grid(row= 5, column= 1)
janela.mainloop()