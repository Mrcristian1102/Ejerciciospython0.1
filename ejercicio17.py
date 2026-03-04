km = float(input("Ingrese km recorridos: "))
minutos = float(input("Ingrese los minutos: "))

if minutos < 10:
    pagar = 5000
else:
    pagar = 800 * km

print(f"Su total a pagar es de: ${pagar}")