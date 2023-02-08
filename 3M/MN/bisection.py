from math import e as euler

def f(c):
    return ((68.1 * 9.81) / c) * (1 - euler**-((c/68.1) * 10)) - 40

def bisection(xi,xu, iteration):
    for i in range(iteration):
            print("\nINTERATION\t",i+1)
            print(f"INTERVALO:\t{xi} | {xu}")
            print(f"f({xi}) = {f(xi)} | f({xu} = {f(xu)})")
            xr = (xi + xu) / 2

            print(f"\nAPROXIMACIÓN:\t{xr}")
            print(f"f({xr}) = {f(xr)}") 

            if f(xi) * f(xr) < 0:
                xu = xr

            if f(xi) * f(xr) > 0:
                xi = xr

            if f(xi) * f(xr) == 0:
                 print("\nRAÍZ ENCONTRADA\n")
                 print(f"f({xi}) * f({xr})")
                 print(f"{f(xi)} * {f(xr)} = {f(xi) * f(xr)}")
                 break
            
bisection(float(input("Establecer valor inicial inferior (xi):\t")),float(input("Establecer valor inicial superior (xu):\t")),int(input("Establecer numero de iteraciones:\t")))
