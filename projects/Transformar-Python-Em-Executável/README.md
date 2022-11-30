# Transformar arquivo Python em executável

O código em si não gera o executável, mas, uma dependência que gera.

## Dependências necessárias

NOTA! Este projeto necessita de uma dependência e recomendo usar um ambiente virtual.

- [PyInstaller](https://pyinstaller.org/en/stable/) - O PyInstaller agrupa um aplicativo Python e todas as suas dependências em um único pacote, gerando o executável.

Para este código recomendo o uso de um [ambiente virtual](../README.md#ambiente-virtual). No [README](../README.md) da pasta [`projects`](../) mostra como criar e ativar.

Para instalar a dependência é só rodar no terminal:

```bash
pip install pyinstaller
```

## Gerar o executável

Após ter criado e ativado o ambiente virtual com a dependência instalada vamos criar o executável. Só Rodar no terminal:

```bash
pyinstaller --onefile ./Executável.py
```

- O comando `pyinstaller` chama a biblioteca.
- O [`--onefile`](https://pyinstaller.org/en/stable/usage.html#cmdoption-F) junta todas as dependências e o código Python em um único arquivo executável.
- No [`./Executável.py`](Executavel.py) você irá colocar o nome do seu programa Python.

Após o comando, terá duas pastas e um arquivo criado, o executável vai estar na pasta `dist`.

Para mais informações encontre na documentação do [PyInstaller](https://pyinstaller.org/en/stable/usage.html#using-pyinstaller).
