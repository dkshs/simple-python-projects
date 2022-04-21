# NOTA!: Necessário a blibioteca 'requests' para fazer a requisição na API.

# ------ Só rodar no terminal `pip install requests` ----
# ---- Leia o README.md desta pasta para mais informações ----

import requests

# -- Fazendo a requisição na API através de GET --
# -- esse link pode mudar se os donos da API mudarem -- 
cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes_dic = cotacoes.json()
cotacao_dolar = cotacoes_dic['USDBRL']['bid']   # Cotação do Dolar para Real
cotacao_bitcoin = cotacoes_dic['BTCBRL']['bid'] # Cotação dp Bitcoin para Real
cotacao_euro = cotacoes_dic['EURBRL']['bid']    # Cotação do Euro para Real
print(cotacao_dolar)
print(cotacao_euro)
print(cotacao_bitcoin)