from tabulate import tabulate as tb

headers1 = ["X1","EA1","X2","EA2","X3","EA3"]
headers2 = ["E1","E2","E3"]
table = []
table_final = []

def e_abs(x_new, x_pre):
    return (abs((x_new - x_pre) / x_new)) * 100

x1 = 0
x2 = 0
x3 = 0
e = 1
eq_x1 = input("Escriba la ecuación despejada 1: ")
eq_x2 = input("Escriba la ecuación despejada 2: ")
eq_x3 = input("Escriba la ecuación despejada 3: ")


while True:
    nx1 = eval(eq_x1)
    e1 = e_abs(nx1,x1)
    nx2 = eval(eq_x2)
    e2 = e_abs(nx2,x2)
    nx3 = eval(eq_x3)
    e3 = e_abs(nx3,x3)
    
    table.append([nx1,e1,nx2,e2,nx3,e3])
    x1 = nx1; x2 = nx2; x3 = nx3

    if e1 < e1 and e2 < e and e3 < e:
        eq_original = input()
        eq_original_2 = input()
        eq_original_3 = input()
        nuevoeq1 = eval(eq_original)
        nuevoeq2 = eval(eq_original_2)
        nuevoeq3 = eval(eq_original_3)
        ef1,ef2,ef3 = [e_abs(nuevoeq1,eq_original),e_abs(nuevoeq2,eq_original_2),e_abs(nuevoeq3,eq_original_3)]
        table_final.append(ef1,ef2,ef3)
        break
    
    
print(tb(table,headers1))
print(tb(table_final,headers2))

