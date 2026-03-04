precio = float(input("Precio del producto: $ "))
if precio > 100000:
    descuento = precio * 0.10
    precio_final = precio - descuento
    print(f"Su descuento es: ${descuento:.2f}")
    print(f"Precio final con descuento: ${precio_final:.2f}")
else:
    print(f"Su precio sin descuento es de: ${precio:.2f}")