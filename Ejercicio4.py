#Crea un programa que pida al usuario dos números y muestre su división si el segundo no es cero, o un mensaje de aviso en caso contrario.
#Fecha: 17/11/2026
#Nombre: Saad Jlilou

a = float(input("Introduce el primer numero: "))
b = float(input("Introduce el segundo numero: "))

if b != 0:
    print("La division es :", a/b)
else:
    print("Aviso no se puede dividir")