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
        valores[i].append(i) # iteracion
        valores[i].append(funtion(a)) # funcion evaluado con a (xi)
        valores[i].append(derivate(a)) # derivada evaluada con a (xo)

        raiz = a - (funtion(a) / derivate(a))
        
        valores[i].append(raiz) # raiz: a - funcion / derivada
        
        error = abs(((a - (funtion(a) / derivate(a))) - a) / (a - (funtion(a) / derivate(a))))
        
        valores[i].append(error)
        valores[i].append(error * 100)
        
        a = raiz # asigna la ultima raiz a la x (xi)
    return valores

encabezado = ["i","fx","derivate","a + 1","e","e%"]
print(tb(NR(int(input("Iteraciones:\t")),int(input("Valor inicial:\t"))),encabezado))