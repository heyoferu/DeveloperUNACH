from math import log as ln
from tabulate import tabulate as tb

def nrIter(iterations,xi):
    f = lambda xi: xi * ln(xi) - 5
    dx = lambda xi: 1 + ln(xi)


    values = {}
    for i in range(iterations):

        values[f"{i}"] = []
        mainFunction = f(xi)
        derivateFunction = dx(xi)
        aproxRoot = xi - (mainFunction / derivateFunction)
        relError = (aproxRoot - xi) / aproxRoot
        xi = aproxRoot

        values[f"{i}"].append(mainFunction)
        values[f"{i}"].append(derivateFunction)
        values[f"{i}"].append(aproxRoot)
        values[f"{i}"].append(relError)
        values[f"{i}"].append(relError * 100)

    return values

hdrs = ["i","fx","dx","xi + 1","e","e%"]

while True:
    try:
        print()
        print("*".center(100,"*"))
        print(" Newton-Rapshon Method ".center(100,"*"))
        print("*".center(100,"*"))
        print()
        print("Choose one:\n\t(1) Set number of iterations")

        try:
            a = int(input())
        except ValueError:
            continue

        match a:
                      
            case 1:
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

                table = nrIter(i,n)
                print(tb(table.values(),hdrs, showindex=True, stralign="center", numalign="left", disable_numparse=True, tablefmt="grid"))
                

    except KeyboardInterrupt:
        break

