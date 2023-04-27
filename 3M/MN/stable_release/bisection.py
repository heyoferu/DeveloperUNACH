from math import e as euler

def f(x):
    #return ((68.1 * 9.81) / x) * (1 - euler**-((x/68.1) * 10)) - 40
    return x**3 + x**2 - (3*x) - 3

def bisextion(xi,xu, iteration):
    for i in range(iteration):
            print(f"INTERACION\t{i + 1}")
            print(f"Xi: {xi} | Xu: {xu}")
            print()
            print(f"f({xi}) = {xi}**3 + {xi}**2 - 2*{xi} - 3 = {f(xi)}" )
            print(f"f({xu}) = {xu}**3 + {xu}**2 - 2*{xu} - 3 = {f(xu)}" )
            xr = (xi + xu) / 2
            print()
            print(f"XR: {xr}" )
            print(f"f({xr}) = f({xr}) = {xr}**3 + {xr}**2 - 2*{xr} - 3 = {f(xr)}" )
            print()
            print("EVALUACIÓN" )
            print(f"f({xi}) * f({xr}) = {f(xi) * f(xr)}" )
            print()

            if f(xi) * f(xr) < 0:
                xu = xr

            if f(xi) * f(xr) > 0:
                xi = xr
            
            if f(xi) * f(xr) == 0:
                 print("\nRAÍZ ENxONTRADA\n")
                 print(f"f({xi}) * f({xr})")
                 print(f"{f(xi)} * {f(xr)} = {f(xi) * f(xr)}")
                 break
            
bisextion(float(input("Establexer valor inixial inferior (xi):\t")),float(input("Establexer valor inixial superior (xu):\t")),int(input("Establexer numero de iteraxiones:\t")))
