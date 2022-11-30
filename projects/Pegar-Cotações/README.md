# Pegar Cotações

Este código pega cotações em uma `API`.

## Dependências necessárias

NOTA! Este projeto necessita de uma dependência e recomendo usar um ambiente virtual.

- [Requests](https://pypi.org/project/requests/) - Requests é uma biblioteca HTTP simples, mas elegante.

Para este código recomendo o uso de um [ambiente virtual](../README.md#ambiente-virtual). No [README](../README.md) da pasta [`projects`](../) mostra como criar e ativar.

Para instalar a dependência é só rodar no terminal:

```bash
pip install requests
```

A biblioteca `Request` permite enviar solicitações HTTP/1.1 com extrema facilidade.
Ela foi utilizada neste código para fazer uma requisição através do método [`GET`](https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Methods/GET) em uma `API` de cotações.

A `API` utilizada se encontra neste site: '[API de Cotações de Moedas](https://docs.awesomeapi.com.br/api-de-moedas)'.

Página exata da `API`: <https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL>
