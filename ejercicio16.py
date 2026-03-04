nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))

promedio = ( nota1 + nota2 + nota3 ) / 3

if promedio <= 60:
    print("Usted ha aprobadó")
elif 55 <= promedio < 29:
    print("Usted ha aprobadó con dificultad")
else:
    print("Usted ha reprobó")

print(f"Su promedio es: {promedio}")