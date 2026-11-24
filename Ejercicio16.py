#La política de cobro de una compañía telefónica es: cuando se realiza una llamada, el
#cobro es por el tiempo que ésta dura, de tal forma que los primeros cinco minutos cuestan
#1 euro, los siguientes tres, 80 céntimos, los siguientes dos minutos, 70 céntimos, y a partir
#del décimo minuto, 50 céntimos. Además, se carga un impuesto de 3 % cuando es
#domingo, y si es otro día, en turno de mañana, 15 %, y en turno de tarde, 10 %. Realice
#un algoritmo para determinar cuánto debe pagar por cada concepto una persona que
#realiza una llamada.
#Nombre: Saad Jlilou
#Fecha : 24/11/2026
minutos = int(input("Minutos de llamada: "))
dia = input("Domingo (D), mañana (M) o tarde (T): ").upper()

costo = 0
for m in range(1, minutos + 1):
    if m <= 5:
        costo = costo + 1
    elif m <= 8:
        costo = costo + 0.80
    elif m <= 10:
        costo = costo + 0.70
    else:
        costo = costo + 0.50

if dia == "D":
    impuesto = costo * 0.03
elif dia == "M":
    impuesto = costo * 0.15
else:
    impuesto = costo * 0.10

print(f"Llamada: {costo:.2f} €")
print(f"Impuesto: {impuesto:.2f} €")
print(f"Total: {costo + impuesto:.2f} €")