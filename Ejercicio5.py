#Escribe un programa que pida un nombre de usuario y una contraseña y si se ha introducido “pepe” y “asdasd” se indica “Has entrado al sistema”, sino se da un error.
#Fecha:17/11/2026
#Nombre:Saad Jlilou

usuario=input("Ingrese su usuario: ")
contraseña=input("Ingrese su contraseña: ")

if usuario == "pepe" and contraseña == "asdasd":
    print("Has entrado al sistema")
else:
    print("error")


