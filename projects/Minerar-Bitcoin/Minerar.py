from hashlib import sha256
import time

# Aplicando a criptografia SHA256
def aplicar_sha256(texto):
    return sha256(texto.encode("ascii")).hexdigest()


# Função que minera o Bitcoin
def minerar(num_bloco, transacoes, hash_anterior, qtde_zeros):
    nonce = 0
    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)
        meu_hash = aplicar_sha256(texto)
        if meu_hash.startswith("0" * qtde_zeros):
            return [nonce, meu_hash]
        nonce += 1


# Chamando a Função minerar com os valores do parâmetro
if __name__ == "__main__":
    num_bloco = 23  # Número do Bloco para minerar
    transacoes = """
    Transações feita no bloco"""  # As transações feita no bloco
    qtde_zeros = 3  # Quantidade de zeros
    hash_anterior = "007deb53d1c463"  # A Hash encontrada do bloco anterior
    inicio = time.time()  # Iniciando um contador
    resultado = minerar(
        num_bloco, transacoes, hash_anterior, qtde_zeros
    )  # Função minerar
    print(f"Nonce: {resultado[0]} || Hash: {resultado[1]}")
    print(f"Tempo demorado: {time.time() - inicio}")
