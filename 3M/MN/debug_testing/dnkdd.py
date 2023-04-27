from math import e, log
from tabulate import tabulate as tb

def funtion(x):
    # return e ** -x -x
    return x * log(x)   - 5

def derivate(x):
    # return -e ** -x -1
    return 1 + log(x)

def NR(c,a):
    valores = []
    for i in range(c):
        valores.append([])
        valores[i].append(i)
        valores[i].append(funtion(a))
        valores[i].append(derivate(a))
        valores[i].append(a - (funtion(a) / derivate(a)))
        valores[i].append(abs(((a - (funtion(a) / derivate(a))) - a) / (a - (funtion(a) / derivate(a)))))
        valores[i].append(abs(((a - (funtion(a) / derivate(a))) - a) / (a - (funtion(a) / derivate(a)))) * 100)
        a = a - (funtion(a) / derivate(a))
    return valores

encabezado = ["i","fx","derivate","a + 1","e","e%"]
print(tb(NR(int(input("Iteraciones:\t")),int(input("Valor inicial:\t"))),encabezado))