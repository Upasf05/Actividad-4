import tkinter as tk #Librería Tkinter para interfaces gráficas

expression = "" #Expresión para almacenar los números que se introduzcan

def press(num): #Función que construye expresión matemática
    global expression    expression += str(num)
    equation.set(expression)

def equalpress(): #Función que analiza la expresión matemática y la muestra en pantalla
    try: #Verificar si se introdujo un número válido
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set("error")
        expression = ""

def clear(): #Función que limpía la expresión en pantalla
    global expression
    expression = ""
    equation.set("")

def delete(): #Función que elimina limina un número en pantalla
    global expression
    expression = expression[:-1]
    equation.set(expression)

if __name__ == "__main__": #Función donde se ejecuta la calculadora
    gui = tk.Tk()
    gui.configure(background="#565a58")
    gui.title("Simple Calc")
    gui.geometry("350x260")  #Ajusta el tamaño de la ventana

    equation = tk.StringVar()

    # Títulos del programa
    left_label = tk.Label(gui, text="ITECSUR, CALCULADORA", font=("Arial", 10, "bold"), bg="#565a58", fg="white") #Primer texto
    left_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="w")  # A la izquierda

    right_label = tk.Label(gui, text="PATRICIO SUÁREZ", font=("Arial", 10, "bold"), bg="#565a58", fg="white") #Segundo texto
    right_label.grid(row=0, column=3, columnspan=2, padx=10, pady=10, sticky="e")  # A la derecha

    
    expression_field = tk.Entry(gui, textvariable=equation, bg="#a2b886", justify='right')
    expression_field.grid(columnspan=5, ipadx=80, padx=10)  # Margen horizontal (padx)

    # Distribución de botones
    #Fila 1
    tk.Button(gui, text=' 1 ', bg='black', fg='white', command=lambda: press(1), height=1, width=7).grid(row=2, column=0, padx=5, pady=5) #Botones númericos
    tk.Button(gui, text=' 2 ', bg='black', fg='white', command=lambda: press(2), height=1, width=7).grid(row=2, column=1, padx=5, pady=5)
    tk.Button(gui, text=' 3 ', bg='black', fg='white', command=lambda: press(3), height=1, width=7).grid(row=2, column=2, padx=5, pady=5)
    tk.Button(gui, text='DEL', bg='black', fg='white', command=delete, height=1, width=7).grid(row=2, column=3, padx=5, pady=5)  #Botón para borrar un número
    tk.Button(gui, text='AC', bg='black', fg='white', command=clear, height=1, width=7).grid(row=2, column=4, padx=10, pady=5) #Botón para limpiar la pantalla

    #Fila 2
    tk.Button(gui, text=' 4 ', bg='black', fg='white', command=lambda: press(4), height=1, width=7).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(gui, text=' 5 ', bg='black', fg='white', command=lambda: press(5), height=1, width=7).grid(row=3, column=1, padx=5, pady=5)
    tk.Button(gui, text=' 6 ', bg='black', fg='white', command=lambda: press(6), height=1, width=7).grid(row=3, column=2, padx=5, pady=5)
    tk.Button(gui, text=' + ', bg='black', fg='white', command=lambda: press("+"), height=1, width=7).grid(row=3, column=3, padx=5, pady=5) #Botones para operaciones
    tk.Button(gui, text=' - ', bg='black', fg='white', command=lambda: press("-"), height=1, width=7).grid(row=3, column=4, padx=10, pady=5)

    #Fila 3
    tk.Button(gui, text=' 7 ', bg='black', fg='white', command=lambda: press(7), height=1, width=7).grid(row=4, column=0, padx=5, pady=5)
    tk.Button(gui, text=' 8 ', bg='black', fg='white', command=lambda: press(8), height=1, width=7).grid(row=4, column=1, padx=5, pady=5)
    tk.Button(gui, text=' 9 ', bg='black', fg='white', command=lambda: press(9), height=1, width=7).grid(row=4, column=2, padx=5, pady=5)
    tk.Button(gui, text=' * ', bg='black', fg='white', command=lambda: press("*"), height=1, width=7).grid(row=4, column=3, padx=5, pady=5)

    tk.Button(gui, text=' 0 ', bg='black', fg='white', command=lambda: press(0), height=1, width=7).grid(row=5, column=0, padx=5, pady=5)
    tk.Button(gui, text=' = ', bg='black', fg='white', command=equalpress, height=1, width=16).grid(row=5, column=1, columnspan=2, padx=5, pady=5)

    gui.mainloop() #Bucle para ejecutar la aplicación

