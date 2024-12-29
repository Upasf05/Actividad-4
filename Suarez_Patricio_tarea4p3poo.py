import tkinter as tk  # Librería Tkinter para interfaces gráficas

class SimpleCalculator: #Clase principal del programa
    def __init__(self, root): 
        self.root = root
        self.root.configure(background="#565a58")
        self.root.title("Calculadora")
        self.root.geometry("350x260")

        self.expression = ""
        self.equation = tk.StringVar()

        self.create_widgets()

    def press(self, num): #Método que construye expreión matemática
        """Construye la expresión matemática."""
        self.expression += str(num)
        self.equation.set(self.expression)

    def equalpress(self): #Método que analiza expresión matemática
        """Evalúa la expresión matemática y la muestra."""
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = ""
        except:
            self.equation.set("Error")
            self.expression = ""

    def clear(self): #Método que limpia la expresión en pantalla
        """Limpia la expresión en pantalla."""
        self.expression = ""
        self.equation.set("")

    def delete(self): #FMétodo que elimina un número en pantalla
        """Elimina el último número en pantalla."""
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def create_widgets(self): #Método que crea la ventana
        """Crea los widgets de la interfaz gráfica."""
        # Título superior
        tk.Label(self.root, text="ITECSUR, CALCULADORA", font=("Arial", 10, "bold"), bg="#565a58", fg="white").grid(row=0, column=0, columnspan=3, pady=10, sticky="w")
        tk.Label(self.root, text="PATRICIO SUÁREZ", font=("Arial", 10, "bold"), bg="#565a58", fg="white").grid(row=0, column=3, columnspan=2, padx=10, pady=10, sticky="e")

        # Campo de entrada
        tk.Entry(self.root, textvariable=self.equation, bg="#a2b886", justify='right').grid(columnspan=5, ipadx=80, padx=10)

        # Distribución de botones
        buttons = [
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('DEL', 2, 3, self.delete), ('AC', 2, 4, self.clear),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('+', 3, 3), ('-', 3, 4),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
            ('0', 5, 0), ('=', 5, 1, self.equalpress, 16)
        ]

        for btn in buttons: #Configurar los botones
            text = btn[0]
            row = btn[1]
            col = btn[2]
            command = btn[3] if len(btn) > 3 else lambda t=text: self.press(t)
            colspan = btn[4] if len(btn) > 4 else 7
            tk.Button(self.root, text=f' {text} ', bg='black', fg='white', command=command, height=1, width=colspan).grid(row=row, column=col, padx=5, pady=5, columnspan=(colspan // 7))

if __name__ == "__main__": #Función if que permite la ejecución del código
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
