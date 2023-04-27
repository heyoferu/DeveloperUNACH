from math import e, log
from tabulate import tabulate as tb

def f(x):
    # return e ** -x -x
    return x * log(x) - 5

def d(x):
    # return -e ** -x -1
    return 1 + log(x)

def metodoNR(it,v):
    valores = []
    i = 0
    while i<=it: 
        valores.append([])
        valores[i].append(i)
        valores[i].append(f(v))
        valores[i].append(d(v))
        valores[i].append(v - (f(v) / d(v)))
        valores[i].append(abs(((v - (f(v) / d(v))) - v) / (v - (f(v) / d(v)))))
        valores[i].append(abs(((v - (f(v) / d(v))) - v) / (v - (f(v) / d(v)))) * 100)
        v = v - (f(v) / d(v))

        i += 1
    return valores

i = int(input("Numero de iteraciones:\t"))
v = int(input("Valor inicial:\t"))
tabla = metodoNR(i,v)
encabezado = ["i","f(x)","f'(x)","v+1","error","error %"]
print(tb(tabla,encabezado))