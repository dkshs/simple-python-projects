# NOTA! A biblioteca 'tkinter' e 'datetime' não precisam ser baixadas por já virem com o Python.
# ---- Leia o README.md desta pasta para mais informações ----

from tkinter import *
from tkinter import ttk
import datetime as dt

lista_tipos = ["Galão", "Caixa", "Saco"]

# ----> Lista onde será armazenada as informações dos materiais:
lista_codigos = []

janela = Tk()

# ----> Função que armazena as informações dos materiais:
def inserir_codigo():
    # ----> Pegando as informações entregues:
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    quant = entry_quant.get()

    # ----> Pegando a data no momento da criação do material:
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M")

    # ----> Criando um código tipo Id:
    codigo = len(lista_codigos) + 1
    codigo_str = "COD-{}".format(codigo)

    # ----> Inserindo as informações em forma de tupla na lista_codigos:
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao))


janela.title("Ferramenta de cadastro de materiais")
# janela.geometry("400x400")

label_descricao = Label(text="Descrição do material")
label_descricao.grid(row=0, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

entry_descricao = Entry()
entry_descricao.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

label_tipo_unidade = Label(text="Tipo da unidade do material")
label_tipo_unidade.grid(row=2, column=0, padx=1, pady=10, sticky="nswe", columnspan=2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(
    row=2, column=2, padx=1, pady=10, sticky="nswe", columnspan=2
)

label_quant = Label(text="Quantidade na unidade de material")
label_quant.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

entry_quant = Entry()
entry_quant.grid(row=3, column=2, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_criar_codigo = Button(text="Criar código", command=inserir_codigo)
botao_criar_codigo.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

janela.mainloop()

print(lista_codigos)
