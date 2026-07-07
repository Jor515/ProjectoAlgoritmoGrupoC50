# ===========================
# VALIDACIONES DEL SISTEMA
# ===========================

# Función para validar que el usuario ingrese un texto.
# No permite números ni campos vacíos.
def validar_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto == "":
            print("Error: no puede dejar el campo vacío.")
        elif not texto.replace(" ", "").isalpha():
            print("Error: solo se permiten letras.")
        else:
            return texto.title()


# Función para validar números enteros positivos.
def validar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Error: ingrese un número mayor que cero.")

        except ValueError:
            print("Error: debe ingresar un número entero.")


# Función para validar números decimales positivos.
def validar_decimal(mensaje):
    while True:
        try:
            numero = float(input(mensaje))

            if numero > 0:
                return numero
            else:
                print("Error: ingrese un valor mayor que cero.")

        except ValueError:
            print("Error: debe ingresar un número válido.")


# Valida teléfonos.
# Solo acepta números y entre 8 y 15 dígitos.
def validar_telefono():
    while True:
        telefono = input("Teléfono: ").strip()

        if telefono.isdigit() and 8 <= len(telefono) <= 15:
            return telefono
        else:
            print("Error: teléfono inválido.")


# Valida la zona de reparto.
def validar_zona():
    zonas = ["Centro", "Norte", "Sur", "Este", "Oeste"]

    while True:

        print("\nZonas disponibles:")

        for zona in zonas:
            print("-", zona)

        ingreso = input("Zona: ").capitalize()

        if ingreso in zonas:
            return ingreso
        else:
            print("Error: zona inexistente.")


# Valida estados del pedido.
def validar_estado():
    estados = [
        "Pendiente",
        "En preparación",
        "En camino",
        "Entregado",
        "Cancelado"
    ]

    while True:

        print("\nEstados disponibles:")

        for i in range(len(estados)):
            print(f"{i+1}. {estados[i]}")

        try:
            opcion = int(input("Seleccione un estado: "))

            if 1 <= opcion <= len(estados):
                return estados[opcion-1]
            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número.")