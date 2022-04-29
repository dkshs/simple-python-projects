# Minerador de Bitcoin

Código que simula uma mineração de Bitcoin.

## Dependências necessárias

NOTA! Este projeto não necessita instalações de bibliotecas.

Abaixo tem as bibliotecas `hashlib` e `time` que são utilizadas. Elas são bibliotecas padrões do Python.

- [haslib](https://docs.python.org/3/library/hashlib.html) - Este módulo implementa uma interface comum para muitos algoritmos de hash seguro e resumo de mensagens diferentes.
- [time](https://docs.python.org/3/library/time.html?highlight=time#module-time) - Este módulo fornece várias funções relacionadas ao tempo.

No biblioteca [`haslib`](https://docs.python.org/3/library/hashlib.html) utilizo somente o [`sha256`](https://docs.python.org/3/library/hashlib.html?highlight=sha256) por isso utilizo o [`from hashlib import sha256`](Minerar.py#L1).

## Gerar o resultado

Entre no código [`Minerar.py`](Minerar.py) e no final terá um [`if`](Minerar.py#L19) com os parâmetros que irá ser enviado e recebido pela função [`minerar`](Minerar.py#L9), tente trocar eles e rodar o código.
