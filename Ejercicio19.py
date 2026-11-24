#Escribe un programa que pida un número entero entre uno y doce e imprima el número
#de días que tiene el mes correspondiente
#Nombre: Saad Jlilou
#Fecha : 24/11/2026

mes = int(input("Mes (1 al 12): "))

if mes == 2:
    print("Tiene 28 días (29 si es bisiesto).")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    print("Tiene 30 días.")
elif 1 <= mes <= 12:
    print("Tiene 31 días.")
else:
    print("ERROR: mes incorrecto.")