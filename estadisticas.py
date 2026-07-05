from pedidos import pedidos, menu_pizzas, zonas_envio

# --------------------------------------------------
# Mostrar estadísticas generales
# --------------------------------------------------

def mostrar_estadisticas():

    if len(pedidos) == 0:
        print("\nNo hay pedidos registrados.")
        return

    total_pedidos = len(pedidos)

    entregados = 0
    pendientes = 0
    en_preparacion = 0
    en_camino = 0
    cancelados = 0

    recaudacion = 0
    
    ventas_por_pizza = {pizza["nombre"]: 0 for pizza in menu_pizzas.values()}
    
    zonas_contador = {zona: 0 for zona in zonas_envio}
    
    for pedido in pedidos:
        zonas_contador[pedido["zona"]] += 1

  

    # Recorrer todos los pedidos
    for pedido in pedidos:

        # Contar estados
        if pedido["estado"] == "Pendiente":
            pendientes += 1

        elif pedido["estado"] == "En preparación":
            en_preparacion += 1

        elif pedido["estado"] == "En camino":
            en_camino += 1

        elif pedido["estado"] == "Entregado":
            entregados += 1
            recaudacion += pedido["total"]

        elif pedido["estado"] == "Cancelado":
            cancelados += 1

        # Contar pedidos por zona
        zonas_envio[pedido["zona"]] += 1
        
        #contar porciones vendidas por tipo de pizza
        for producto in pedido["productos"]:
            if producto["nombre"] in ventas_por_pizza:
                ventas_por_pizza[producto["nombre"]] += producto["porciones"]

    promedio = recaudacion / total_pedidos
    
    # Buscar la pizza más vendida
    pizza_mas_vendida = ""
    mayor_ventas = 0
    
    for nombre_pizza, porciones in ventas_por_pizza.items():
        if porciones > mayor_ventas:
            mayor_ventas = porciones
            pizza_mas_vendida = nombre_pizza
    

    # Buscar la zona con más pedidos
    zona_mayor = ""
    mayor = 0

    for zona in zonas_envio:

        if zonas_envio[zona] > mayor:

            mayor = zonas_envio[zona]
            zona_mayor = zona

    # Mostrar resultados
    print("\n========== ESTADÍSTICAS ==========")
    
    print("-----------------------------------")
    print("Porciones vendidas por tipo de pizza:")

    for pizza, porciones in ventas_por_pizza.items():
        print(f"{pizza}: {porciones}")

    print("-----------------------------------")
    
    print(f"Pedidos registrados : {total_pedidos}")
    print(f"Pendientes          : {pendientes}")
    print(f"En preparación      : {en_preparacion}")
    print(f"En camino           : {en_camino}")
    print(f"Entregados          : {entregados}")
    print(f"Cancelados          : {cancelados}")

    print("-----------------------------------")

    print(f"Recaudación total   : ${recaudacion:.2f}")
    print(f"Promedio por pedido : ${promedio:.2f}")

    print("-----------------------------------")

    print("Pedidos por zona:")

    for zona in zonas_envio:

        print(f"{zona}: {zonas_envio[zona]}")

    print("-----------------------------------")

    print("Zona con más pedidos:", zona_mayor)
    print("Pizza más vendida:", pizza_mas_vendida)