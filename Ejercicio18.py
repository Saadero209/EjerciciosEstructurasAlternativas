#Realiza un programa que pida el día de la semana (del 1 al 7) y escriba el día
#correspondiente. Si introducimos otro número nos da un error
#Nombre : Saad Jlilou
#Fecha : 24/11/2026

n = int(input("Día de la semana (1 al 7): "))

if n == 1:
    print("Lunes")
elif n == 2:
    print("Martes")
elif n == 3:
    print("Miércoles")
elif n == 4:
    print("Jueves")
elif n == 5:
    print("Viernes")
elif n == 6:
    print("Sábado")
elif n == 7:
    print("Domingo")
else:
    print("ERROR: número incorrecto.")