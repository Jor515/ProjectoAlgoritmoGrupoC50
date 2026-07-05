# ============================
# VALIDACIONES DEL SISTEMA
# ============================


#validar que el usuario ingrese bien la opcion del menu
def validar_opcion_menu(menu):
    while True:
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion in menu:
                return opcion
            else:
                print("Opción inválida. Intente nuevamente.")
                
        except ValueError:
            print("Error: debe ingresar un número entero.")
            
#Validar que se ingrse bien la canrtidad de porciones
def validar_cantidad_porciones(maximo):
    while True:
        try:
            cantidad = int(input(f"cantidad de porciones (1 a {maximo}):"))
            
            if 1 <= cantidad <= maximo:
                return cantidad
            else:
                print(f"Error: ingrese un número entre 1 y {maximo}.")
                
        except ValueError:
            print("Error: debe ingresar un número entero.")
        
                
            
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
#def validar_zona(zonas_disponibles):
#    while True:
#        print("\nZonas disponibles:")
#        for zona in zonas_disponibles:
#            print("-", zona)
            
#        ingreso = input("zona: ").title()
        
#        if ingreso in zonas_disponibles:
#            return ingreso
#        else:
#            print("Error: zona inexistente. Intente nuevamente.")

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