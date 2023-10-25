"""Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a 
aplicar y calcule e imprima por pantalla el precio final del artículo.
"""
iva =float(0.21) 
num1 = int(input("Precio primer producto: "))
print(num1)
num2 = int(input("Precio segundo producto: "))
print(num2)
iva = 0.21
suma = num1 + num2
costeiva = iva * suma
coniva = costeiva + suma

print(f"Sin iva la suma de los productos es: {suma}")

print(f"Con iva incluido el costo es: {coniva}")
