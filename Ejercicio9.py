#Algoritmo que pida tres números y los muestre ordenados (de mayor a menor);
#Fecha: 17/11/2026
#Nombre: Saad jlilou

a=float(input("Ingrese el valor del a : "))
b=float(input("Ingrese el valor del b : "))
c=float(input("Ingrese el valor del c : "))

if a< b:
    a, b = b, a
if a< c:
    a, c = c, a
if b< c:
    b, c = c, b

print("De mayor a menor", a, b, c)