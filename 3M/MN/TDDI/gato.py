import tkinter as tk

# Set up the window
window = tk.Tk()
window.title("Fractal Tree")
window.geometry("500x500")

# Set up the canvas
canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

# Define the recursive function for drawing the fractal tree
def draw_fractal(x, y, length, angle, depth):
    if depth == 0:
        return
    
    # Calculate the end point of the line
    x2 = x + int(length * tk.cos(tk.radians(angle)))
    y2 = y - int(length * tk.sin(tk.radians(angle)))
    
    # Draw the line
    canvas.create_line(x, y, x2, y2, width=depth, fill="#")
    
    # Recursively call the function to draw the branches
    draw_fractal(x2, y2, length*0.7, angle-25, depth-1)
    draw_fractal(x2, y2, length*0.7, angle+25, depth-1)

# Call the recursive function to draw the fractal tree
draw_fractal(250, 450, 100, -90, 10)

# Start the main loop
window.mainloop()
