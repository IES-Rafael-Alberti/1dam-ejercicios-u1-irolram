"""
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final 
de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en 
la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla 
la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
"""
intereses = 0.04
inversion = float(input("Introduce la inversión inicial: "))
primeranio = inversion * (1 + intereses)
print("primer año de intereses: ",primeranio)
print("segundo año intereses: ", (primeranio * (1 + intereses)))
segundoanio = primeranio * (1 + intereses)
print("tercer año intereses: ", segundoanio * (1 + intereses))

