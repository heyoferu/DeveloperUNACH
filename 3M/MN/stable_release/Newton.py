from prettytable import PrettyTable
from sympy import diff, Symbol
from math import *

tabla = PrettyTable()


def root_eval(ec,dx):
    return x - (ec / dx)

ecuacion = input("Escriba la ecuación:\t")

var = Symbol('x')

derivada = diff(ecuacion, var)
print(derivada)

x_a = 0
x = float(input("Valor inicial:\t"))

# tabla.field_names = ["f(x)","f'(x)","xn"]
tabla.field_names = ["i",ecuacion,str(derivada),"xn"]
i = 0
while True:
    ec_eval = eval(ecuacion)
    dx_eval = eval(str(derivada))
    root = root_eval(ec_eval,dx_eval)
    
    x_a = x
    x = root

    tabla.add_row([i,ec_eval,dx_eval,x])

    if x_a == x:
        break
    i += 1
print(tabla)
    