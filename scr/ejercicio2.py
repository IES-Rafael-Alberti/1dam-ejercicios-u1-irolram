"""Escribe un programa para pedirle al 
usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.
"""

numhora = int(input("¿Cuántas horas trabajas al día?: "))
print(numhora)
dinero = int(input("¿Cuánto dinero ganas a la hora?: "))
print(dinero)

print("Usted gana al día",numhora * dinero  )
