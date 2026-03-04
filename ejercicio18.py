ancho = float(input("Valor del ancho: "))
largo = float(input("Valor del largo: "))

area = ancho * largo

if area < 12:
    tamaño = "pequeño"

elif area <= 20:
    tamaño = "mediano"

else:
    tamaño = "grande"

print(f"Área = {area} m2")
print(f"Tamaño: {tamaño}")