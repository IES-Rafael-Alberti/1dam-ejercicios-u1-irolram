"""
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades 
y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 
6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 
dígitos enteros y 2 decimales.
"""
producto = input("Introduzca nombre del producto: \n")
precio = float(input("Introduce el precio del producto: \n"))
unidad = int(input("Introduce las unidades del producto: \n"))

print("{producto}: cuesta {precio:4.2f}€ y las unidades son {unidad:1d} = {total:2.2f}€".format(producto = producto, unidad = unidad, precio = precio, total = precio * unidad))
