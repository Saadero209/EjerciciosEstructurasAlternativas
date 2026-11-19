#Algoritmo que pida los puntos centrales x1,y1,x2,y2 y los radios r1,r2 de dos circunferencias y las clasifique en uno de estos estados: • exteriores • tangentes exteriores • secantes • tangentes interiores • interiores • concéntricas
#Fecha: 19/11/2026
#Nombre: Saad Jlilou

x1 = float(input("Ingrese el valor del x1 : "))
y1 = float(input("Ingrese el valor del y1 : "))
r1 = float(input("Ingrese el valor del r1 : "))
x2 = float(input("Ingrese el valor del x2 : "))
y2 = float(input("Ingrese el valor del y2 : "))
r2 = float(input("Ingrese el valor del r2 : "))

d = (x2 - x1) ** 2 + (y2 - y1) ** 2
suma = (r1 + r2) ** 2
resta = (r1 - r2) ** 2

if d == 0:
    print("concéntricas")
elif d > suma:
    print("exteriores")
elif d == suma:
    print("tangentes exteriores")
elif d > resta:
    print("secantes")
elif d == resta:
    print("tangentes interiores")
else:
    print("interiores")


