import time  # Para dar um tempo entre um print e outro

db = {}
print("Bem-vindo ao banco de dados de valor mais simples")
time.sleep(1)
while True:
    print("O que você quer fazer?")
    time.sleep(0.5)
    print('Coloque "P" para colocar, "G" para Pegar ou "L" para listar')
    print('Ou coloque "Q" para sair')
    action = input()
    if action == "P":
        k = input("Coloque a key: ")
        d = input("Coloque o dado: ")
        db[k] = d
        print("Inserindo...")
        time.sleep(1)
        print("Dado inserido")
        time.sleep(0.5)
    elif action == "G":
        k = input("Coloque a key: ")
        print("Procurando...")
        time.sleep(1)
        if not k in db:
            print("Nenhuma key encontrada")
            time.sleep(1)
        else:
            print("Seu dado é: %s" % db[k])
            time.sleep(1)
    elif action == "L":
        print("Carregando dados...")
        time.sleep(1)
        print("Itens de DB:")
        print(db)
        time.sleep(1)
    elif action == "Q":
        print("Tchau")
        break
