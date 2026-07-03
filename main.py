from pedidos import (
    registrar_pedido,
    mostrar_pedidos,
    buscar_pedido,
    cambiar_estado,
    eliminar_pedido
)

from estadisticas import mostrar_estadisticas

def mostrar_menu():

    print("\n")
    print("=" * 40)
    print("      PIZZA EXPRESS DELIVERY      ")
    print("=" * 40)

    print("1. Registrar pedido")
    print("2. Mostrar pedidos")
    print("3. Buscar pedido")
    print("4. Cambiar estado")
    print("5. Eliminar pedido")
    print("6. Estadísticas")
    print("7. Salir")

    print("=" * 40)

# Programa
def main():

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            registrar_pedido()

        elif opcion == "2":

            mostrar_pedidos()

        elif opcion == "3":

            buscar_pedido()

        elif opcion == "4":

            cambiar_estado()

        elif opcion == "5":

            eliminar_pedido()

        elif opcion == "6":

            mostrar_estadisticas()

        elif opcion == "7":

            print("\nGracias por utilizar Delivery Express.")
            print("Hasta luego.")

            break

        else:

            print("\nOpción inválida. Intente nuevamente.")


main()