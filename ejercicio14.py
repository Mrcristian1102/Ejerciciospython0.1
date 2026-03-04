temperatura = int(input("Temperatura actual: "))
if temperatura <= 15:
    print(f"Temperatura actual: {temperatura} hace frio")
elif temperatura >= 28:
    print(f"Temperatura actual: {temperatura} hace calor")
else:
    print("Temperatura agradable")