"""
Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el
IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
"""

pro1 = float(input("Precio del articulo: "))
print(pro1)
iva = float(0.10)
coniva = pro1 * iva
sumaiva =float(coniva + pro1)
print("El articulo cuesta: ")
print(pro1)
print("Coste del IVA: ")
print(coniva)
print("El coste del IVA sumado al articulo es: ")
print(sumaiva)