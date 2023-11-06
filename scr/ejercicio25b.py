fechana = input("Introduce tu fecha ed nacimiento en el formato dia/mes/año: ")

dia = fechana[:fechana.find("/")]
mesaño = fechana[fechana.find('/')+1:]
mes = mesaño[:mesaño.find("/")]
año = mesaño[:mesaño.find("/")+1:]
print("dia", dia)
print("mes", mes)
print("año", año)