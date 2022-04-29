# NOTA! Necessário a biblioteca 'pandas' para exportar os clientes em um arquivo excel.
# A biblioteca 'tkinter' e 'sqlite3' não precisam ser baixadas por já virem com o Python.

# Esse código eu recomendo criar um ambiente virtual para resultados melhores.
# ------ Só rodar no terminal `pip install pandas` ----
# ---- Leia o README.md desta pasta para mais informações ----

import tkinter as tk
import sqlite3
import pandas as pd


# -------- Criar banco de dados -----------

# conexao = sqlite3.connect('banco_clientes.db')

## -----> Criando o cursor:
# c = conexao.cursor()

## -----> Criando a tabela:
# c.execute(''' CREATE TABLE clientes (
#     nome text,
#     sobrenome text,
#     email text,
#     telefone text
# )
# ''')

## ------> Commit as mudanças:
# conexao.commit()

## ------> Fechar o banco de dados:
# conexao.close()


# ----------- Criando Janela -----------

janela = tk.Tk()
janela.title('Cadastro de Clientes')
janela. geometry("350x350")
label_error = tk.Label(janela, text='')

def cadastrar_cliente():
    conexao = sqlite3.connect('banco_clientes.db')
    c = conexao.cursor()
    
    # -----> Informações das entradas:
    cliente_nome = entry_nome.get()
    cliente_sobrenome = entry_sobrenome.get()
    cliente_email = entry_email.get()
    cliente_telefone = entry_telefone.get()
    
    # -----> Verificando o email:
    sql = """SELECT email FROM clientes WHERE email = ?"""
    usrEmail_Search = c.execute(sql, (cliente_email,)).fetchone()
    
    # -----> Verificando campos vazios:
    if cliente_nome == '' or cliente_sobrenome == '' or cliente_email == '' or cliente_telefone == '':
        label_error.config(text='Os campos não podem ser vazios', fg='red')
        label_error.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)
    # -----> Verificando se já tem email cadastrado:
    elif usrEmail_Search:
        label_error.config(text='Email já cadastrado', fg='red')
        label_error.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)
    else:
    # -----> Inserindo os dados depois de passar pelas verificações:
        c.execute('INSERT INTO clientes VALUES (:nome,:sobrenome,:email,:telefone)',
                {
                    'nome': cliente_nome,
                    'sobrenome': cliente_sobrenome,
                    'email': cliente_email,
                    'telefone': cliente_telefone
                }
                )
        
        conexao.commit()
        conexao.close()
        
        entry_nome.delete(0, 'end')
        entry_sobrenome.delete(0, 'end')
        entry_email.delete(0, 'end')
        entry_telefone.delete(0, 'end')
        
        label_error.config(text='Cliente salvo', fg='green')
        label_error.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)


def exporta_clientes():
    conexao = sqlite3.connect('banco_clientes.db')
    c = conexao.cursor()

    c.execute('SELECT oid, * FROM clientes')
    clientes_cadastrados = c.fetchall()
    clientes_cadastrados = pd.DataFrame(clientes_cadastrados, columns=['id_banco', 'nome', 'sobrenome', 'email', 'telefone'])
    clientes_cadastrados.to_excel('banco_clientes.xlsx')
    
    conexao.commit()
    conexao.close()
    
    label_error.config(text='Expotação concluida', fg='green')
    label_error.grid(row=4, column=0, columnspan=2, padx=10, pady=10, ipadx=80)


# ------> Rótulos Entradas:
label_nome = tk.Label(janela, text='Nome')
label_nome.grid(row=0, column=0, padx=10, pady=10)

label_sobrenome = tk.Label(janela, text='Sobrenome')
label_sobrenome.grid(row=1, column=0, padx=10, pady=10)

label_email = tk.Label(janela, text='E-mail')
label_email.grid(row=2, column=0, padx=10, pady=10)

label_telefone = tk.Label(janela, text='Telefone')
label_telefone.grid(row=3, column=0, padx=10, pady=10)


# ------> Caixas Entradas:
entry_nome = tk.Entry(janela, width=35)
entry_nome.grid(row=0, column=1, padx=10, pady=10)

entry_sobrenome = tk.Entry(janela, width=35)
entry_sobrenome.grid(row=1, column=1, padx=10, pady=10)

entry_email = tk.Entry(janela, width=35)
entry_email.grid(row=2, column=1 , padx=10, pady=10)

entry_telefone = tk.Entry(janela, width=35)
entry_telefone.grid(row=3, column=1, padx=10, pady=10)


# -----> Botão de Cadastrar

botao_cadastrar = tk.Button(text='Cadastrar Cliente', command=cadastrar_cliente)
botao_cadastrar.grid(row=5, column=0, columnspan=2, padx=10, pady=10 , ipadx=80)


# -----> Botão de Exportar

botao_exportar = tk.Button(text='Exportar para Excel', command=exporta_clientes)
botao_exportar.grid(row=6, column=0, columnspan=2, padx=10, pady=10 , ipadx=80)


janela.mainloop()