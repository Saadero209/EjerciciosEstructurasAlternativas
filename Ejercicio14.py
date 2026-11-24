#La asociación de vinicultores tiene como política fijar un precio inicial al kilo de uva, la
#cual se clasifica en tipos A y B, y además en tamaños 1 y 2. Cuando se realiza la venta
#del producto, ésta es de un solo tipo y tamaño, se requiere determinar cuánto recibirá un
#productor por la uva que entrega en un embarque, considerando lo siguiente: si es de tipo
#A, se le cargan 20 céntimos al precio inicial cuando es de tamaño 1; y 30 céntimos si es
#de tamaño 2. Si es de tipo B, se rebajan 30 céntimos cuando es de tamaño 1, y 50 céntimos
#cuando es de tamaño 2. Realice un algoritmo para determinar la ganancia obtenida.
#Fecha: 19/11/2026
#Nombre: Saad Jlilou

precio = float(input("Precio inicial por kilo (€): "))
kilos = float(input("Kilos de uva: "))
tipo = input("Tipo (A o B): ").upper()
tamaño = int(input("Tamaño (1 o 2): "))

if tipo == "A" and tamaño == 1:
    precio = precio + 0.20
elif tipo == "A" and tamaño == 2:
    precio = precio + 0.30
elif tipo == "B" and tamaño == 1:
    precio = precio - 0.30
elif tipo == "B" and tamaño == 2:
    precio = precio - 0.50
else:
    print("Tipo o tamaño malo.")
    exit()

ganancia = precio * kilos
print(f"Precio final por kilo: {precio:.2f} €")
print(f"El productor recibe: {ganancia:.2f} €")