# -8*x1 +x2 -2*x3 = -20,2*x1 -6*x2 -x3 = -38,-3*x1 -x2 +7*x3 = -34
# (-20 -x2 +2*x3)/-8,(-38 -2*x1 +x3)/-6,(-34 +3*x1 +x2)/7

from prettytable import PrettyTable
table = PrettyTable()
results = PrettyTable()
table.field_names = ["Iteración", "X1", "Ea1", "X2", "Ea2","X3", "Ea3",]
results.field_names = ["Función original", "Comprobación", "Error absoluto"]

def inputs(text):
    data = input(f"{text}: \t")
    return data.split(",")

abError = lambda xn, xa : abs(((xn-xa)/xn)*100)

print("*** GAUSS SEIDEL ***\nIngrese los siguientes datos separados por comas:\n")

initialV = [0,0,0]
punctuations = inputs("FUNTIONS PUNTUACTIONS")
print(punctuations)
pE = int(input("ERROR PERCENT:\t\t"))    
fWithoutC = []

c=0
while c <=3:
    c += 1

    newX = []
    error = []
    eX = []
    print(f"\nITERACIÓN {c}")
    for i in range(3):
        x1 = float(initialV[0])
        x2 = float(initialV[1])
        x3 = float(initialV[2])

        evaluation = eval(punctuations[i])
        newX.append(evaluation)

        initialV.pop(i)
        initialV.insert(i,evaluation)

        x = [x1,x2,x3]
        e = abError(newX[i],x[i])
        print(e)
        eX.append(e)
    
    print(eX)
     # Añade valores a la tabla principal

    table.add_row([c, newX[0], f"{eX[0]} %", newX[1], f"{eX[1]} %", newX[2], f"{eX[2]} %"])

print(table)
