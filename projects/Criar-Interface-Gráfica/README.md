# Interfaces Gráficas

Alguns códigos que geram interfaces gráficas.

## Dependências necessárias

NOTA! Este projeto tem dois códigos, no [`interface.py`](interface.py) não é necessário instalações, mas no [`Cadastro_clientes.py`](Cadastro_clientes.py) é necessário a instalação do [`pandas`](https://pandas.pydata.org/) e recomendo o uso de um [ambiente virtual](../#ambiente-virtual).

Abaixo tem as bibliotecas utilizadas que não precisam ser baixadas por já virem com o Python:

- [tkinter](https://docs.python.org/3/library/tkinter.html) - Pacote que cria interfaces gráficas. Utilizo em ambos os códigos.

- [datetime](https://docs.python.org/3/library/datetime.html) - O módulo `datetime` fornece classes para manipulação de datas e horas. Utilizo no código [`interface.py`](interface.py) para pegar a data.

- [sqlite3](https://docs.python.org/3/library/sqlite3.html) - Criador e manipulador de bancos SQLite. Utilizo no código [`Cadastro_clientes.py`](Cadastro_clientes.py) para gerar e manipular um banco de dados SQLite.

Agora a única biblioteca necessária a baixar caso for utilizar o código [`Cadastro_clientes.py`](Cadastro_clientes.py):

- [pandas](https://pandas.pydata.org/) - Ferramenta de análise e manipulação de dados de código aberto rápida, poderosa, flexível e fácil de usar. Utilizo no código [`Cadastro_clientes.py`](Cadastro_clientes.py) para conseguir exportar as informações do `db` para um arquivo excel.

Para o código [`Cadastro_clientes.py`](Cadastro_clientes.py) recomendo o uso de um [ambiente virtual](../#ambiente-virtual). No [README](../#ambiente-virtual) da pasta [`projects`](../) mostra como criar e ativar.

> Caso não queira instalar o pandas ou usar um ambiente virtual é só remover a função `exportar_clientes` e o ultimo botão do [`Cadastro_clientes.py`](Cadastro_clientes.py).

Para instalar a dependência é só rodar no terminal:

```bash
pip install pandas
```

## 🚀 Rodar o Código

Ultima configuração se você for rodar o código [`Cadastro_clientes.py`](Cadastro_clientes.py). É necessário ter o banco de dados SQLite, no começo do código, após as importações você verá o comentário 'Criar banco de dados', descomente eles e rode o código para gerar o DB, após gerado pode comentar essas linhas para não ficar gerando um DB toda hora.
Pronto agora só rodar código! 🚀
