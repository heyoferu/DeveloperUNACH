from prettytable import PrettyTable
from sympy import symbols,solve,parse_expr

table = PrettyTable()
headers = []

e_abs = lambda x_new, x_old: (abs((x_new - x_old) / x_new)) * 100

eqs = input("Ecuaciones separadas por coma:\t").split(",")

xn = input("Escribir las xn desde 1 hasta n:\t").split(",")
eq_solved = []
xn_values = []
toAdd = []

for i in range(len(xn)):
    headers.append(xn[i])
    headers.append(f"E{i+1}")

for i in range(len(xn)):
    xn_values.append(float(input(f"Escribir valor de {xn[i]}:\t")))

for i in range(len(eqs)): # this an auto solver for each eq
    x = symbols(xn[i])
    eq_temp = solve(parse_expr(eqs[i].split("=")[0]) - parse_expr(eqs[i].split("=")[1]),x)[0]
    eq_solved.append(str(eq_temp))

for eq in range(len(eq_solved)):
    for i in range(len(xn)):
        temp = eq_solved[eq].replace(xn[i],f"xn_values[{i}]")
        eq_solved[eq] = temp

while True:
    toAdd.clear()
    for i in range(len(xn)):
        x_old = xn_values[i]
        x_new = eval(eq_solved[i])
        error = e_abs(x_new,x_old)

        toAdd.append(x_new)
        toAdd.append(error)

        xn_values[i] = x_new

    table.add_row(toAdd)

    if round(x_old) == round(x_new):
        break

table.field_names = headers
print(table)