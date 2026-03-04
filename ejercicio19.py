usuario = input("Nombre de usuario: ")
contraseña = input("Digite su contraseña: ")

U = "admin"
c = "1234"

if usuario == U and contraseña == c:
    print("Acceso concedido")
else:
    print("Acceso denegado")