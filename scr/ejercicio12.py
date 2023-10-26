"""
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal
y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales
"""

peso = float(input("Introduzca su peso en kg:\n "))

estatura = float(input("Introduzca su altura en metros:\n "))

print("Su indice de masa corporal es: ",(peso) / (estatura) ** 2)