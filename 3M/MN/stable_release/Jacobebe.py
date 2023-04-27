from tabulate import tabulate
from sympy import symbols,solve,parse_expr

encabezado = ["X1","EA1","X2","EA2","X3","EA3"]

def absoluto_e(xnueva, xanterior):
    return abs((xnueva - xanterior) / xnueva) * 100

table = []
table_error = []
ecuacion_1 = input("Ecuacion original 1:\t")
ecuacion_2 = input("Ecuacion original 2:\t")
ecuacion_3 = input("Ecuacion original 3:\t")
x1 = symbols('x1')
x2 = symbols('x2')
x3 = symbols('x3')
ecuacion_1_f = parse_expr(ecuacion_1.split("=")[0]) - parse_expr(ecuacion_1.split("=")[1])
ecuacion_2_f = parse_expr(ecuacion_2.split("=")[0]) - parse_expr(ecuacion_2.split("=")[1])
ecuacion_3_f = parse_expr(ecuacion_3.split("=")[0]) - parse_expr(ecuacion_3.split("=")[1])
ecuacion_despejada_1 = solve(ecuacion_1_f,x1)
ecuacion_despejada_2 = solve(ecuacion_2_f,x2)
ecuacion_despejada_3 = solve(ecuacion_3_f,x3)

error = float(input("Type the error percent:\t"))
x1 = input("Valor inicial 1: ")
x2 = input("Valor inicial 2: ")
x3 = input("Valor inicial 3: ")

while True:
    x1_calculada = eval(str(ecuacion_despejada_1[0]))
    error_1 = absoluto_e(x1_calculada,x1)
    x2_calculada = eval(str(ecuacion_despejada_2[0]))
    error_2 = absoluto_e(x2_calculada,x2)
    x3_calculada = eval(str(ecuacion_despejada_3[0]))
    error_3 = absoluto_e(x3_calculada,x3)
    
    table.append([x1_calculada,error_1,x2_calculada,error_2,x3_calculada,error_3])
    x1 = x1_calculada
    x2 = x2_calculada
    x3 = x3_calculada

    if error_1 < error and error_2 < error and error_3 < error:
        eq_or1 = ecuacion_1.split('=') 
        eq_or2 = ecuacion_2.split('=')
        eq_or3 = ecuacion_3.split('=') 
        errorfinal1 = absoluto_e(eval(eq_or1[0]),int(eq_or1[1]))
        errorfinal2 = absoluto_e(eval(eq_or2[0]),int(eq_or2[1]))
        errorfinal3 = absoluto_e(eval(eq_or3[0]),int(eq_or3[1]))
        
        table_error.append([errorfinal1,errorfinal2,errorfinal3])
        break
    
    
print(tabulate(table,encabezado))
print(tabulate(table_error))

