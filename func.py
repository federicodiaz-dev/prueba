def fibo(lista,a,b):
    for i in range(6):
        c = a+b
        lista.append(c)
        a = b
        b = c
    return lista

lista = []

fibo(lista, 0,1)


for i in range(len(lista)):
    print(lista[i], end=' ')