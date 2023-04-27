from prettytable import PrettyTable
from sympy import symbols,solve,parse_expr

table = PrettyTable(); table.field_names = ["X1","EA1","X2","EA2","X3","EA3"]
table_error = PrettyTable(); table_error.field_names = ["Final_E1","Final_E2","Final_E3"]

e_abs = lambda x_new, x_pre: (abs((x_new - x_pre) / x_new)) * 100

eqs_main = input("Type the equations separated by comma:\t").split(",")

x1,x2,x3 = symbols('x1 x2 x3')
eq_x1 = solve(parse_expr(eqs_main[0].split("=")[0]) - parse_expr(eqs_main[0].split("=")[1]),x1)
eq_x2 = solve(parse_expr(eqs_main[1].split("=")[0]) - parse_expr(eqs_main[1].split("=")[1]),x2)
eq_x3 = solve(parse_expr(eqs_main[2].split("=")[0]) - parse_expr(eqs_main[2].split("=")[1]),x3)

e = float(input("Type the error percent:\t"))
v = input("Type the initial value:\t").split(",")
x1 = int(v[0]); x2 = int(v[1]); x3 = int(v[2])

while True:
    new_x1 = eval(str(eq_x1[0]))
    e1 = e_abs(new_x1,x1)
    new_x2 = eval(str(eq_x2[0]))
    e2 = e_abs(new_x2,x2)
    new_x3 = eval(str(eq_x3[0]))
    e3 = e_abs(new_x3,x3)
    
    table.add_row([new_x1,e1,new_x2,e2,new_x3,e3])
    x1 = new_x1; x2 = new_x2; x3 = new_x3

    if all(ei < e for ei in [e1, e2, e3]):
        eq_or1 = eqs_main[0].split('=') 
        eq_or2 = eqs_main[1].split('=')
        eq_or3 = eqs_main[2].split('=') 
        eq1_new = eval(eq_or1[0])
        eq2_new = eval(eq_or2[0])
        eq3_new = eval(eq_or3[0])
        print(eq1_new)
        print(eq2_new)
        print(eq3_new)
        table_error.add_row([e_abs(eq1_new,int(eq_or1[1])),e_abs(eq2_new,int(eq_or2[1])),e_abs(eq3_new,int(eq_or3[1]))])
        break
    
    
print(table); print(table_error)

