"""
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día.
Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una 
constante), el descuento que se le hace por no ser fresca y el coste 
final total de todas las barras no frescas.
"""
pan = 3.49
pana =round(3.49 * 0.6, 2)

vendidas = float(input("Nº de barras vendidas que no son del día:\n "))
print("La barra de hoy cuesta: ", pan)
print("Si no es fresca la barra cuesta: ", pana)
print("El coste total de las barras no frescas vendidas es de: ",(pana * vendidas),"euros")