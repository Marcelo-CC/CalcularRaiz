import tkinter as tk
from tkinter import messagebox
import math


class CalculadoraRaizCuadradaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Raíz Cuadrada")

        # Etiqueta de entrada
        self.label = tk.Label(root, text="Introduce un número:")
        self.label.pack(pady=10)

        # Entrada de texto
        self.entrada = tk.Entry(root)
        self.entrada.pack(pady=5)

        # Botón para calcular la raíz cuadrada
        self.boton_calcular = tk.Button(root, text="Calcular Raíz Cuadrada", command=self.calcular_raiz)
        self.boton_calcular.pack(pady=10)

        # Etiqueta para mostrar el resultado
        self.resultado = tk.Label(root, text="")
        self.resultado.pack(pady=10)

    def calcular_raiz(self):
        try:
            numero = float(self.entrada.get())
            if numero < 0:
                mensaje = "No se puede calcular la raíz cuadrada de un número negativo"
            else:
                raiz_cuadrada = math.sqrt(numero)
                mensaje = f"La raíz cuadrada de {numero} es: {raiz_cuadrada:.2f}"
        except ValueError:
            mensaje = "Por favor, introduce un número válido."

        # Mostrar el resultado en un cuadro de mensaje
        self.resultado.config(text=mensaje)


# Crear la ventana principal
root = tk.Tk()
app = CalculadoraRaizCuadradaApp(root)
root.mainloop()
