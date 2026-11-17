#Programa que lea una cadena por teclado y compruebe si es una letra mayúscula.
#Fecha:17/11/2026
#Nombre: Saad Jlilou

Cadena = input("Ingrese su texto: ")

if any(letra.upper() in Cadena for letra in Cadena):
    print("El texto es Mayuscula")
else:
    print("El texto es Miniscula")