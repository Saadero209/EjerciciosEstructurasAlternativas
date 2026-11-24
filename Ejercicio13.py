#Escribe un programa que pida una fecha (día, mes y año) y diga si es correcta
#Fecha: 19/11/2026
#Nombre: Saad Jlilou
from datetime import datetime

dia = int(input("Día: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

try:
    datetime(año, mes, dia)
    print("Fecha correcta.")
except ValueError:
    print("Fecha incorrecta.")