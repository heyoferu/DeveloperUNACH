from sympy import symbols, solve, parse_expr

eqstr =  ["6 * x1 + 2 * x2 + x3 = 22", "-x1 + 8 * x2 + 2 * x3 = 30", "x1 - x2 + 6 * x3 = 23"]
x1,x2,x3 = symbols('x1 x2 x3')
eq = parse_expr(eqstr[0].split("=")[0]) -  parse_expr(eqstr[0].split("=")[1])
sol = solve(eq,x1)


a = 0 
b = 0 
c = 0 
# print(eval(sol[0]))
print(eval(str(sol[0])))

# eqor1 = input("Insert the equation 1:\t") # = (22-2*x2-x3)/6
# eqor2 = input("Insert the equation 2:\t") # = (30+x1-2*x3)/8
# eqor3 = input("Insert the equation 3:\t") # = (23-x1+x2)/6

# 6 * x1 + 2 * x2 + x3 = 22, -x1 + 8 * x2 + 2 * x3 = 30, x1 - x2 + 6 * x3 = 23 