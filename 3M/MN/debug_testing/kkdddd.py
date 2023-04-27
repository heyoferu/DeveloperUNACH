from math import log
from tabulate import tabulate

def f(x):
    return x * log(x)   - 5

def d(x):
    return 1 + log(x)

def metodoNewtonRaphson(vueltas,xi):
    
    tabla = []
    for i in range(vueltas):
        tabla.append([0,0,0,0,0,0])
        
        # iteracion
        tabla[i][0] = i

        # xi evaluada en f(x)
        funcion = f(xi)
        tabla[i][1] = funcion

        # xi evaluada en d(x)
        derivada = d(xi)
        tabla[i][2] = derivada

        # raiz aproximada; xi - (funcion / derivada)
        raiz = xi - (funcion / derivada)
        tabla[i][3] = raiz

        # error
        error = abs((raiz - xi) / raiz)

        errorpercent = error * 100
        
        tabla[i][4] = error
        tabla[i][5] = errorpercent
        
        xi = raiz # asigna la ultima raiz xi la x (xi)
    return tabla

print(
    tabulate(metodoNewtonRaphson(int(input("Iteraciones para el metodo:\t")),
          int(input("Valor inicial para la función:\t"))),["i","fx","d","xi + 1","e","e%"],
          numalign="left",
          disable_numparse=True)
)

tabla = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
]