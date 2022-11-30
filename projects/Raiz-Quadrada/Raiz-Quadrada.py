def qrange(n):
    for i in range(1, n):
        yield i * i


n = 10
print("A raiz quadrada de 1 a %d é:" % (n - 1))
for i in qrange(n):
    print(i)
