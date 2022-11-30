import smtplib
import email.message

# --- Enviar email ---
def enviar_email():
    corpo_email = f"""
    <h1>Hello World!</h1>
    <p>Aqui posso colocar código HTML</p>
    <button>Clica aqui</button>
    """

    msg = email.message.Message()
    msg["Subject"] = "Assunto do Email"  # Este é o Assunto do Email
    msg["From"] = "email@email.com"  # Conta que irá enviar o Email
    msg["To"] = "email@email.com"  # Pessoa ou pessoas que irá receber o Email
    password = "senha123"  # Senha da conta do "FROM"
    msg.set_type("text/html")
    msg.set_payload(corpo_email)

    s = smtplib.SMTP("smtp.gmail.com: 587")
    s.starttls()
    s.login(msg["From"], password)
    s.sendmail(msg["From"], [msg["To"]], msg.as_string().encode("utf-8"))
    print("email enviado")


enviar_email()
