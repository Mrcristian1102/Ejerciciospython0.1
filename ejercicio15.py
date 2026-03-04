sueldo_mensual = float(input("Ingrese su sueldo mensual: $"))

if sueldo_mensual < 1500000:
    impuesto = 0
    sueldo_neto = sueldo_mensual

elif sueldo_mensual <= 3000000:
    impuesto = sueldo_mensual * 0.05
    sueldo_neto = sueldo_mensual - impuesto

else:
    impuesto = sueldo_mensual * 0.10
    sueldo_neto = sueldo_mensual - impuesto

print(f"Impuesto a pagar: $ {impuesto}")
print(f"Sueldo neto: $ {sueldo_neto}")