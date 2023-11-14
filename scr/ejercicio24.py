"""
Escribir un programa que pregunte por consola el precio de un producto en euros con 
dos decimales y muestre por pantalla el número de euros y el número de céntimos del
precio introducido.
"""
precio = input("Introduce el precio del producto con decimales:  ")
print(precio[:precio.find('.')], "euros y" , precio[precio.find(".")+1:], "céntimos.") 
#el +1 es para quitar el punto
