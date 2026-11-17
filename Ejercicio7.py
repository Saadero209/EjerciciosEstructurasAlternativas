#Realiza un algoritmo que calcule la potencia, para ello pide por teclado la base y el exponente. Pueden ocurrir tres cosas: • El exponente sea positivo, sólo tienes que imprimir la potencia. • El exponente sea 0, el resultado es 1. • El exponente sea negativo, el resultado es 1/potencia con el exponente positivo.
#Fecha: 17/11/2026
#Nombre: Saad Jlilou

base = float(input("Ingrese el valor de base: "))
expoente = float(input("Ingrese el valor de expoente: "))

if expoente > 0:
    print("El resultado es :", base ** expoente)
elif expoente == 0:
    print("El resultado es :", 1)
else:
    if base == 0:
        print("No se puede dividir entre 0")
    else:
        print("El resultado es :",1/(base ** -expoente))



