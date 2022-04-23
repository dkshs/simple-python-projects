# NOTA! Necessário a biblioteca 'qrcode' para criar o Qrcode e 
# 'pillow' para gerar a imagem

# Esse código eu recomendo criar um ambiente virtual para resultados melhores.
# ------ Só rodar no terminal `pip install pillow qrcode` ----
# ---- Leia o README.md desta pasta para mais informações ----

import qrcode

# ------ Forma simples de criar um QrCode com algo específico -------

imagem_qrcode = qrcode.make("link do site")
imagem_qrcode.save("qrcode_phyton.png")


# ------ Forma de criar vários QrCodes de uma vez usando `For` -----

codigos_links={
    "Youtube":"youtube.com",
    "Texto":"TextoTeste"}

for site in codigos_links:
    link = codigos_links[site]
    imagem_qrcode = qrcode.make(link)
    imagem_qrcode.save(f"QrCode_{site}.png")
