numero1 = int(input("Numero 1:  "))
numero2 = int(input("Numero 2:  "))

if numero1 == numero2:
    print(f"Es igual el {numero1},que el {numero2} ")
elif numero1 > numero2:
    print(f"Numero mayor es: {numero1}")
    print(f"Numero mmenor es: {numero2}")    
else:
    print(f"Numero mayor es:  {numero2}")
    print(f"Numero menor es: {numero1}")