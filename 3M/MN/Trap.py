import sympy as sp
import numpy as np
import turtle

x = sp.Symbol('x')
ecuacion = input("Ingrese la función en términos de x: ") # x**3 - 6*x**2 + 11*x - 6
f = sp.sympify(ecuacion) #convertir texto a ecuacion

a = float(input("Ingrese el intervalo a: ")) #1.3
b = float(input("Ingrese el intervalo b: ")) #1.8

punto_a = f.subs(x, a)   # paso 1
punto_b = f.subs(x, b)
emp = (b-a)/2 # paso 2
paso3 = emp * (punto_a + punto_b) # paso 3

segundaDerivada = sp.diff(f, x, 2) # paso 4
error = -(1/12) * segundaDerivada.evalf(subs={x: b-a}) * (b-a)**3

print("Intervalo a es: " + str(round(punto_a, 5)))
print("Intervalo b es: " + str(round(punto_b, 5)))
print("Resultado del trapecio: " + str(round(paso3, 5)))
print("Error: " + str(round(error,5)))

# Turtle code to draw the graph
t = turtle.Turtle()
t.penup()
t.goto(-300, 0)
t.pendown()
t.speed(0)
t.forward(600)
t.penup()
t.goto(0, -200)
t.pendown()
t.forward(400)
t.penup()
t.goto(a*100, f.subs(x, a)*100)
t.pendown()
for i in range(int(a*100), int(b*100), 5):
    t.goto(i, f.subs(x, i/100)*100)
t.goto(b*100, f.subs(x, b)*100)
t.penup()
t.goto(0, 220)
t.pendown()
t.write(f"Intervalo a es: {round(punto_a, 5)}")
t.penup()
t.goto(0, 200)
t.pendown()
t.write(f"Intervalo b es: {round(punto_b, 5)}")
t.penup()
t.goto(0, 180)
t.pendown()
t.write(f"Resultado del trapecio: {round(paso3, 5)}")
t.penup()
t.goto(0, 160)
t.pendown()
t.write(f"Error: {round(error, 5)}")
t.hideturtle()
turtle.done()