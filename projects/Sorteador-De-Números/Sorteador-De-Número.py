import random

maxn = 10
tentativas = 3
n = random.randint(1, maxn)
print('Bem vindo ao jogo de advinhar o número!')
print('Escolha um número de 1 até %d' % maxn)
print(f'Você tem {tentativas} tentativas!')
guess = None
while guess != n and tentativas != 0:
    guess = int(input('Sua tentativa: '))
    if guess > n:
        print('Muito alto')
    if guess < n:
        print('Muito baixo')
    tentativas -= 1
    print(f'Você tem {tentativas} tentativas')

if tentativas == 0 and guess != n:
    print('Você perdeu, suas tentivas acabaram!')
else:
    print('Boa, você venceu!')
