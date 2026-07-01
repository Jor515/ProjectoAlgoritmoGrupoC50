from pedidos import pedidos


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

    zonas = {
        "Centro": 0,
        "Norte": 0,
        "Sur": 0,
        "Este": 0,
        "Oeste": 0
    }

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
        zonas[pedido["zona"]] += 1

    promedio = recaudacion / total_pedidos

    # Buscar la zona con más pedidos
    zona_mayor = ""
    mayor = 0

    for zona in zonas:

        if zonas[zona] > mayor:

            mayor = zonas[zona]
            zona_mayor = zona

    # Mostrar resultados

    print("\n========== ESTADÍSTICAS ==========")

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

    for zona in zonas:

        print(f"{zona}: {zonas[zona]}")

    print("-----------------------------------")

    print("Zona con más pedidos:", zona_mayor)