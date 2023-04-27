import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        self.result = tk.StringVar()
        self.result.set("0")
        self.expression = ""

        # Pantalla
        self.screen = tk.Entry(master, textvariable=self.result, justify="right", font=("Arial", 20))
        self.screen.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

        # Botones de la calculadora
        buttons = [
            ("1", 1), ("2", 1), ("3", 1), ("+", 1),
            ("4", 1), ("5", 1), ("6", 1), ("-", 1),
            ("7", 1), ("8", 1), ("9", 1), ("*", 1),
            ("0", 1), ("C", 1), ("=", 2), ("/", 1)
        ]

        # Crear los botones
        r = 1
        c = 0
        for text, width in buttons:
            button = tk.Button(master, text=text, width=width, font=("Arial", 20), command=lambda text=text: self.button_click(text))
            button.grid(row=r, column=c, pady=5, padx=5)
            c += width
            if c >= 4:
                c = 0
                r += 1

    def button_click(self, text):
        if text == "C":
            self.result.set("0")
            self.expression = ""
        elif text == "=":
            try:
                self.result.set(eval(self.expression))
            except:
                self.result.set("ERROR")
            self.expression = ""
        else:
            if self.result.get() == "0":
                self.result.set(text)
            else:
                self.result.set(self.result.get() + text)
            self.expression += text

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
