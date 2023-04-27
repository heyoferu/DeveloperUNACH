from math import e, log
import pandas as pd
from tabulate import tabulate as tb


def f(x):
    return x**3 - 2*x + 1
    #return e ** -x -x
    #return x * log(x) - 5

def dx(x):
    return 3*x**2 - 2
    #return -e ** -x -1
    #return 1 + log(x)

def nrAuto(error,n):
    table = []
    i = 0
    while True:
        table.append([])
        table[i].append(i)
        table[i].append(f(n))
        table[i].append(dx(n))
        table[i].append(n - (f(n) / dx(n)))
        table[i].append(
            abs(
            ((n - (f(n) / dx(n))) - n) / (n - (f(n) / dx(n)))
            )
        )
        table[i].append(
            abs(
            ((n - (f(n) / dx(n))) - n) / (n - (f(n) / dx(n)))
            ) * 100
        )

        if table[i][5] < error:
            break
    
        n = n - (f(n) / dx(n))
        i += 1

    return table

def nrIter(iterations,n):
    table = []

    for i in range(iterations):
        table.append([])
        table[i].append(i)
        table[i].append(f(n))
        table[i].append(dx(n))
        table[i].append(n - (f(n) / dx(n)))
        table[i].append(
            abs(
            ((n - (f(n) / dx(n))) - n) / (n - (f(n) / dx(n)))
            )
        )
        table[i].append(
            abs(
            ((n - (f(n) / dx(n))) - n) / (n - (f(n) / dx(n)))
            ) * 100
        )

    
        n = n - (f(n) / dx(n))

    return table

hdrs = ["i","fx","dx","xi + 1","e","e%"]

while True:
    try:
        print()
        print("*".center(100,"*"))
        print(" Newton-Rapshon Method ".center(100,"*"))
        print("*".center(100,"*"))
        print()
        print("Choose one:\n\t(1) Automatic\n\t(2) Set number of iterations")

        try:
            a = int(input())
        except ValueError:
            continue

        match a:
                      
            case 1:
                while True:
                    try:
                        error = float(input("Value error: "))
                        break
                    except ValueError:
                        continue
                while True:
                    try:
                        n = float(input("Intial value: "))
                        break
                    except ValueError:
                        continue
                print(tb(nrAuto(error,n),hdrs,numalign="center",disable_numparse=True))

            case 2:
                while True:
                    try:
                        i = int(input("Iterations number: "))
                        break
                    except ValueError:
                        continue
                while True:
                    try:
                        n = float(input("Intial value: "))
                        break
                    except ValueError:
                        continue
                print(tb(nrIter(i,n),hdrs,numalign="center", disable_numparse=True))

    except KeyboardInterrupt:
        break