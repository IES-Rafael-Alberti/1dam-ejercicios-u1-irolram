"""
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
nom =input("Escriba su nombre: ")
num =int(input("Escribe un numero entero: "))
for _ in range(num): #El "for _ in" es un bucle 
    print(nom)

