from validaciones import *

# Lista donde se almacenarán todos los pedidos
pedidos = []

# Variable para generar IDs automáticos
ultimo_id = 1

# zonas o barrios de entrega
zonas_envio = {
    1: {"nombre": "Centro", "costo_envio": 800},
    2: {"nombre": "Barrio San Martin", "costo_envio": 1200},
    3: {"nombre": "Villa Rio Negro", "costo_envio": 1500},
    4: {"nombre": "400 Viviendas", "costo_envio": 1800},
    5: {"nombre": "Barranqueras", "costo_envio": 2200},
 }

# menu de pizzas
menu_pizzas = {
    1: {"nombre": "Muzzarella", "precio_porcion": 350},
    2: {"nombre": "Napolitana", "precio_porcion": 420},
    3: {"nombre": "Fugazzeta", "precio_porcion": 400},
    4: {"nombre": "Cuatro Quesos", "precio_porcion": 480},
    5: {"nombre": "Especial", "precio_porcion": 520},
}

# menu para seleccionar pizzas
def mostrar_menu_pizzas():
    print("\n--- Menú de Pizzas ---")
    for numero, pizza in menu_pizzas.items():
        print(f"{numero}. {pizza['nombre']} - ${pizza['precio_porcion']} por porción")
        
Porciones_maxima = 12

def mostrar_menu_zonas():
    print("\n--- Zonas de Entrega ---")
    for numero, zona in zonas_envio.items():
        print(f"{numero}. {zona['nombre']} - Costo de envío: ${zona['costo_envio']}")
        
# Registrar un pedido
def registrar_pedido():

    global ultimo_id

    print("\n===== REGISTRAR PEDIDO =====")

    cliente = validar_texto("Nombre del cliente: ")
    telefono = validar_telefono()

    mostrar_menu_zonas()
    opcion_zona = validar_opcion_menu(zonas_envio)
    zona_elegida = zonas_envio[opcion_zona]
   
    zona = zona_elegida["nombre"]
    envio = zona_elegida["costo_envio"]
   
    direccion = input("Dirección: ").strip()

    while direccion == "":
        print("La dirección no puede estar vacía.")
        direccion = input("Dirección: ").strip()


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

    total = subtotal + envio

    pedido = {
        "id": ultimo_id,
        "cliente": cliente,
        "telefono": telefono,
        "direccion": direccion,
        "zona": zona,
        "productos": productos,
        "subtotal": subtotal,
        "envio": envio,
        "total": total,
        "estado": "Pendiente"
    }

    pedidos.append(pedido)

    print("\nPedido registrado correctamente.")
    print(f"Número de pedido: {ultimo_id}")

    ultimo_id += 1

# Mostrar todos los pedidos
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
                f"${producto['precio']:.2f} = "
                f"${producto['total']:.2f}"
            )

        print("\nSubtotal: $", pedido["subtotal"])
        print("Envío: $", pedido["envio"])
        print("TOTAL: $", pedido["total"])
        print("Estado:", pedido["estado"])


# Buscar pedido por ID
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


# Cambiar estado
def cambiar_estado():

    pedido = buscar_pedido()

    if pedido is None:
        return

    print("\nEstado actual:", pedido["estado"])

    nuevo_estado = validar_estado()

    pedido["estado"] = nuevo_estado

    print("Estado actualizado correctamente.")

# Eliminar pedido
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