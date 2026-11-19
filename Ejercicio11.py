#Programa que lea 3 datos de entrada A, B y C. Estos corresponden a las dimensiones de
#los lados de un triángulo. El programa debe determinar que tipo de triangulo es, teniendo
#en cuenta los siguiente:
#• Si se cumple Pitágoras entonces es triángulo rectángulo
#• Si sólo dos lados del triángulo son iguales entonces es isósceles.
#• Si los 3 lados son iguales entonces es equilátero.
#• Si no se cumple ninguna de las condiciones anteriores, es escaleno
#Fecha: 19/11/2026
#Nombre: Saad Jlilou

a=float(input("Ingrese el valor del a : "))
b=float(input("Ingrese el valor del b : "))
c=float(input("Ingrese el valor del c : "))

if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
    print("rectangulo")
elif a == b == c:
    print("equilatero")
elif a == b or a == c or b == c:
    print("isoceles")
else:
    print("escaleno")