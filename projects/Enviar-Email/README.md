# Enviar Email

Código que envia email por Gmail.

## Dependências necessárias

NOTA! Este projeto não necessita instalações de bibliotecas.

Abaixo tem as bibliotecas `smtplib` e `email.message` que são utilizadas. Elas são bibliotecas padrões do Python.

- [smtplib](https://docs.python.org/3/library/smtplib.html) - O módulo `smtplib` define um objeto de sessão do cliente SMTP que pode ser usado para enviar mensagens para qualquer máquina da Internet com um daemon de escuta SMTP ou ESMTP.
- [email.message](https://docs.python.org/3/library/email.message.html) - `email.message` fornece a funcionalidade principal para definir e consultar campos de cabeçalho, para acessar corpos de mensagens e para criar ou modificar mensagens estruturadas.

## Enviar o Email

Para enviar o email você precisa colocar as informações necessárias sendo o Assunto do Email, a pessoa ou as pessoas que irão receber o email, a conta que irá enviar o email e a senha, também pode modificar o corpo do email na variável `corpo_email`, então só rodar o código.

NOTA! Esse código envia emails somente pelo [Gmail](https://www.google.com/intl/pt/gmail/about/).
