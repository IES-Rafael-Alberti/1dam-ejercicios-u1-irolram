"""
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
funcione cuando el día o el mes se introduzcan con un solo carácter.
"""

fechana = input("Dime la fecha de nacimiento en formato dd/mm/aaaa): \n")
print("Dia", fechana[:2])
print("Mes", fechana[3:5])
print("Año", fechana[6:])


