from validaciones import *

# Lista donde se almacenarán todos los pedidos
pedidos = []

# Variable para generar IDs automáticos
ultimo_id = 1

#menu de pizzas xd
menu_pizzas = {
    1: {"nombre": "Muzzarella", "precio_porcion": 350},
    2: {"nombre": "Napolitana", "precio_porcion": 420},
    3: {"nombre": "Fugazzeta", "precio_porcion": 400},
    4: {"nombre": "Cuatro Quesos", "precio_porcion": 480},
    5: {"nombre": "Especial", "precio_porcion": 520},
}
#menu para seleccionar pizzas
def mostrar_menu_pizzas():
    print("\n--- Menú de Pizzas ---")
    for numero, pizza in menu_pizzas.items():
        print(f"{numero}. {pizza['nombre']} - ${pizza['precio_porcion']} por porción")
        
Porciones_maxima = 12

opcion = validar_opcion_menu(menu_pizzas)
# --------------------------------------------------
# Calcula el costo de envío según la zona
# --------------------------------------------------
def calcular_envio(zona):

    if zona == "Centro":
        return 1000

    elif zona == "Norte":
        return 1500

    elif zona == "Sur":
        return 1800

    elif zona == "Este":
        return 1600

    elif zona == "Oeste":
        return 1700


# --------------------------------------------------
# Registrar un pedido
# --------------------------------------------------
def registrar_pedido():

    global ultimo_id

    print("\n===== REGISTRAR PEDIDO =====")

    cliente = validar_texto("Nombre del cliente: ")
    telefono = validar_telefono()

    direccion = input("Dirección: ").strip()

    while direccion == "":
        print("La dirección no puede estar vacía.")
        direccion = input("Dirección: ").strip()

    zona = validar_zona()

    productos = []

    subtotal = 0

    while True:
        print("\nIngrese los detalles del producto:")
        mostrar_menu_pizzas()
        opcion = validar_opcion_menu(menu_pizzas)       
        Tipo_pizza = menu_pizzas[opcion]
        
        print(f"\n{Tipo_pizza['nombre']} se vende por porción")
        porciones = validar_cantidad_porciones(Porciones_maxima)
        
        total_producto = porciones * Tipo_pizza["precio_porcion"]


        producto = {
            "nombre": Tipo_pizza["nombre"],
            "porciones": porciones,
            "precio": Tipo_pizza["precio_porcion"],
            "total": total_producto
        }

        productos.append(producto)

        subtotal += total_producto

        seguir = input("\n¿Agregar otro producto? (S/N): ").upper()

        if seguir != "S":
            break

    envio = calcular_envio(zona)

    total = subtotal + envio

    pedido = {
        "id": ultimo_id,
        "cliente": cliente,
        "telefono": telefono,
        "direccion": direccion,
        "zona": zona,
        "productos": Tipo_pizza,
        "subtotal": subtotal,
        "envio": envio,
        "total": total,
        "estado": "Pendiente"
    }

    pedidos.append(pedido)

    print("\nPedido registrado correctamente.")
    print(f"Número de pedido: {ultimo_id}")

    ultimo_id += 1


# --------------------------------------------------
# Mostrar todos los pedidos
# --------------------------------------------------
def mostrar_pedidos():

    if len(pedidos) == 0:
        print("\nNo hay pedidos registrados.")
        return

    print("\n========== PEDIDOS ==========")

    for pedido in pedidos:

        print("\n-----------------------------")

        print("Pedido N°:", pedido["id"])
        print("Cliente:", pedido["cliente"])
        print("Teléfono:", pedido["telefono"])
        print("Dirección:", pedido["direccion"])
        print("Zona:", pedido["zona"])

        print("\nProductos:")

        for producto in pedido["productos"]:

            print(
                f"- {producto['nombre']} | "
                f"{producto['porciones']} porciones x "
                f"${producto['precio_porcion']:.2f} = "
                f"${producto['total']:.2f}"
            )

        print("\nSubtotal: $", pedido["subtotal"])
        print("Envío: $", pedido["envio"])
        print("TOTAL: $", pedido["total"])
        print("Estado:", pedido["estado"])


# --------------------------------------------------
# Buscar pedido por ID
# --------------------------------------------------
def buscar_pedido():

    if len(pedidos) == 0:
        print("\nNo existen pedidos.")
        return

    numero = validar_entero("Ingrese el número del pedido: ")

    for pedido in pedidos:

        if pedido["id"] == numero:

            print("\nPedido encontrado.")

            print("Cliente:", pedido["cliente"])
            print("Estado:", pedido["estado"])
            print("Total: $", pedido["total"])

            return pedido

    print("Pedido inexistente.")

    return None


# --------------------------------------------------
# Cambiar estado
# --------------------------------------------------
def cambiar_estado():

    pedido = buscar_pedido()

    if pedido is None:
        return

    print("\nEstado actual:", pedido["estado"])

    nuevo_estado = validar_estado()

    pedido["estado"] = nuevo_estado

    print("Estado actualizado correctamente.")


# --------------------------------------------------
# Eliminar pedido
# --------------------------------------------------
def eliminar_pedido():

    pedido = buscar_pedido()

    if pedido is None:
        return

    respuesta = input(
        "¿Desea eliminar el pedido? (S/N): "
    ).upper()

    if respuesta == "S":

        pedidos.remove(pedido)

        print("Pedido eliminado.")

    else:

        print("Operación cancelada.")