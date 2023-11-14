"""
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre
m da un cociente c y un resto r", donde n y m son los números introducidos 
por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.
"""
n = int(input("Escribe un número:\n"))
m = int(input("Dame otro número:\n"))

resto = (n % m)
cociente = (n // m)

print("El cociente de la suma de los dos numeros es: ", cociente)
print("El resto de la suma de los dos numeros es: ", resto)