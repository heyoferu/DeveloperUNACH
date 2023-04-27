from tabulate import tabulate

x = [0,0,0]
igualdades = [22,30,23]
tabla = []

x1,x2,x3 = x
eq1 = input()
eq2 = input()
eq3 = input()

def eorginales():
    a = eval(eq1)
    b = eval(eq2)
    c = eval(eq3)
    return [a,b,c]

def ec():
    return eval(eq1)

def ec2():
    return eval(eq2)

def ec3():
    return eval(eq3)

def ab(xnuevo, xanterior):
    return (abs((xnuevo - xanterior) / xnuevo)) * 100

e = 1
j = 0

while True:
    x1 = ec(x)
    x2 = ec2(x)
    x3 = ec3(x)

    e1 =  ab(x1,x[0])
    e2 =  ab(x2,x[1])
    e3 =  ab(x3,x[2])

    tabla.append([x1,e1,x2,e2,x3,e3])
    x = [x1,x2,x3]

    if all(ei < e for ei in [e1,e2,e3]):
        error_xns = eorginales(x)
        break


print(tabulate(tabla,["x1","ea","x2","ea","x3","ea"],showindex=True,disable_numparse=True))
print(tabulate([["Ex1",error_xns[0]],["Ex2",error_xns[1]],["Ex3",error_xns[2]]],disable_numparse=True))
