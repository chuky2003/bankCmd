
usuarios = {
    "juan": {
        "contrasena": "prueba",
        "saldo": 1000
    },
    "pablo": {
        "contrasena": "prueba2",
        "saldo": 1500
    },
}


def Login():
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")

    if usuario in usuarios and usuarios[usuario]["contrasena"] == contrasena:
        print("Inicio de sesión exitoso.")
        return usuario
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return None


def insertMoney(usuario):
    cantidad = float(input("Ingrese la cantidad que desea ingresar: "))
    if cantidad > 0:
        usuarios[usuario]["saldo"] += cantidad
        print(f"Se ha ingresado ${cantidad} a su cuenta. Su saldo actual es: ${usuarios[usuario]['saldo']}")
    else:
        print("La cantidad debe ser mayor que cero.")


def extractMoney(usuario):
    cantidad = float(input("Ingrese la cantidad que desea extraer: "))
    if cantidad > 0 and cantidad <= usuarios[usuario]["saldo"]:
        usuarios[usuario]["saldo"] -= cantidad
        print(f"retiró ${cantidad} de su cuenta. su dinero actual es: ${usuarios[usuario]['saldo']}")
    else:
        print("Monto invalido")


def main():
    usuarioActual = None

    while True:
        if usuarioActual is None:
            print("\n1. Iniciar sesión")
            print("2. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                usuarioActual = Login()
            elif opcion == "2":
                break
            else:
                print("Opcion no valida, seleccione de vuelta")
                print("===================================")
        else:
            print("1. Ingresar dinero")
            print("2. Extraer dinero")
            print("3. Cerrar sesion")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                insertMoney(usuarioActual)
            elif opcion == "2":
                extractMoney(usuarioActual)
            elif opcion == "3":
                print("Cuenta cerrada")
                usuarioActual = None
            else:
                print("Opcion no valida, seleccione de vuelta")


main()


