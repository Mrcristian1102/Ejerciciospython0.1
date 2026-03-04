edad = int(input("Digite su edad: "))
estrato = int(input("Digite su estrato: "))

if 18 <= edad <= 25 and estrato in (1, 2, 3):
    print("Aplica el subsidio")

else:
    print("No aplica")