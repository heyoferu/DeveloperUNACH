import sympy as sp
import pygame

# Set up Pygame window
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trapezoidal Rule Graph")

# Set up font for displaying results
font = pygame.font.SysFont("arial", 20)

x = sp.Symbol('x')
ecuacion = input("Ingrese la función en términos de x: ")
f = sp.sympify(ecuacion)

a = float(input("Ingrese el intervalo a: "))
b = float(input("Ingrese el intervalo b: "))

punto_a = f.subs(x, a)
punto_b = f.subs(x, b)
emp = (b-a)/2
paso3 = emp * (punto_a + punto_b)

segundaDerivada = sp.diff(f, x, 2)
error = -(1/12) * segundaDerivada.evalf(subs={x: b-a}) * (b-a)**3

print("Intervalo a es: " + str(round(punto_a, 5)))
print("Intervalo b es: " + str(round(punto_b, 5)))
print("Resultado del trapecio: " + str(round(paso3, 5)))
print("Error: " + str(round(error,5)))

# Set up graph variables
x_offset, y_offset = 100, height - 100
x_scale, y_scale = 50, 50

# Draw x and y axes
pygame.draw.line(screen, (255, 255, 255), (x_offset, y_offset), (width - x_offset, y_offset))
pygame.draw.line(screen, (255, 255, 255), (x_offset, y_offset), (x_offset, 50))

# Draw function graph
for i in range(int(a*x_scale), int(b*x_scale), 5):
    x1 = i/x_scale
    y1 = y_offset - f.subs(x, x1).evalf()*y_scale
    x2 = (i+5)/x_scale
    y2 = y_offset - f.subs(x, x2).evalf()*y_scale
    pygame.draw.line(screen, (0, 255, 0), (x_offset + x1*x_scale, y1), (x_offset + x2*x_scale, y2))

# Draw results on screen
text = font.render(f"Intervalo a es: {round(punto_a, 5)}", True, (255, 255, 255))
screen.blit(text, (20, 20))
text = font.render(f"Intervalo b es: {round(punto_b, 5)}", True, (255, 255, 255))
screen.blit(text, (20, 40))
text = font.render(f"Resultado del trapecio: {round(paso3, 5)}", True, (255, 255, 255))
screen.blit(text, (20, 60))
text = font.render(f"Error: {round(error, 5)}", True, (255, 255, 255))
screen.blit(text, (20, 80))

# Update display and wait for user to close window
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
