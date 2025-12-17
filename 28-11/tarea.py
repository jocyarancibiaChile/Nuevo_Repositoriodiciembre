print("Sistema de Gestión de Reservas - Cine")

peliculas = {
    1: {
        "titulo": "Intensamente 2",
        "funciones": {
            1: {"horario": "12:00", "disponibles": 30, "precio": 4000},
            2: {"horario": "16:00", "disponibles": 25, "precio": 4500},
        },
    },
    2: {
        "titulo": "Las Guerreras K-Pop",
        "funciones": {
            1: {"horario": "14:00", "disponibles": 25, "precio": 4200},
            2: {"horario": "17:00", "disponibles": 35, "precio": 4800},
        },
    },
    3: {
        "titulo": "El Conjuro",
        "funciones": {
            1: {"horario": "19:00", "disponibles": 20, "precio": 4500},
            2: {"horario": "21:30", "disponibles": 25, "precio": 4800},
        },
    },
}

reservas = []
def mostrar_peliculas():
    print("Películas disponibles:")
    for pid, pinfo in peliculas.items():
        print(f"{pid}. {pinfo['titulo']}")
    for fid, finfo in pinfo['funciones'].items():
        print(f" Funcion {fid}: {finfo['horario']} - Disponibles: {finfo['disponibles']} - Precio: $ {finfo['precio']}")
    print()


def seleccionar_pelicula():
    while True:
        try:
            pid = int(input("Ingrese el número de la película (0 para volver al menú): "))
            if pid == 0:
                return None
            if pid in peliculas:
                return pid
            else:
                print("Película no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida — ingrese un número.")


def seleccionar_funcion(pelicula_id):
    funciones = peliculas[pelicula_id]['funciones']
    while True:
        try:
            fid = int(input("Ingrese el número de la función deseada (0 para cancelar): "))
            if fid == 0:
                return None
            if fid in funciones:
                return fid
            else:
                print("Función no válida. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida — ingrese un número.")

def solicitar_cantidad_max(disponibles):
    while True:
        try:
            cantidad = int(input(f"Ingrese la cantidad de boletos (máx {disponibles}, 0 para cancelar): "))
            if cantidad == 0:
                return 0
            if 0 < cantidad <= disponibles:
                return cantidad
            print(f"Cantidad inválida. Debe ser entre 1 y {disponibles}.")
        except ValueError:
            print("Entrada inválida — ingrese un número entero.")

def confirmar_reserva(pelicula_id, funcion_id, cantidad):
    pelicula = peliculas[pelicula_id]
    funcion = pelicula['funciones'][funcion_id]
    subtotal = cantidad * funcion['precio']
    print("\nResumen provisional:")
    print(f"Película: {pelicula['titulo']}")
    print(f"Función: {funcion['horario']}")
    print(f"Boletos: {cantidad}")
    print(f"Precio unitario: $ {funcion['precio']}")
    print(f"Subtotal: $ {subtotal}")

    while True:
        confirmar = input("Confirmar compra? (s/n): ").strip().lower()
        if confirmar in ('s', 'n'):
            break
        print("Respuesta no válida. Responda 's' o 'n'.")

    if confirmar == 's':
        peliculas[pelicula_id]['funciones'][funcion_id]['disponibles'] -= cantidad
        reserva = {
            'pelicula_id': pelicula_id,
            'funcion_id': funcion_id,
            'cantidad': cantidad,
            'subtotal': subtotal,
            }
        reservas.append(reserva)
        print("Reserva confirmada. Gracias!\n")
    else:
        print("Reserva cancelada.\n")

def mostrar_resumen_final():
    if not reservas:
        print("No se realizaron reservas.")
        return
    
    print("\n--- RESUMEN FINAL DE RESERVAS ---")
    total = 0
    for i, r in enumerate(reservas, start=1):
        p = peliculas[r['pelicula_id']]['titulo']
        f = peliculas[r['pelicula_id']]['funciones'][r['funcion_id']]['horario']
        c = r['cantidad']
        s = r['subtotal']
        total += s
        print(f"{i}. {p} | {f} | Boletos: {c} | Subtotal: $ {s}")
    print(f"\nTotal a pagar: $ {total}")
    print("-------------------------------\n")

def main():
    print("Bienvenido al Sistema de Gestión de Reservas - Cine")

    while True:
        print("\nMENU:\n1) Ver películas y horarios\n2) Hacer una reserva\n3) Ver resumen final y salir")
        opcion = input("Seleccione una opción (1/2/3): ").strip()


        if opcion == '1':
            mostrar_peliculas()

        elif opcion == '2':
            mostrar_peliculas()
            pid = seleccionar_pelicula()
            if pid is None:
                continue
            fid = seleccionar_funcion(pid)
            if fid is None:
                continue
            disponibles = peliculas[pid]['funciones'][fid]['disponibles']
            if disponibles <= 0:
                print("Lo sentimos, no hay boletos disponibles para esa función.")
                continue
            cantidad = solicitar_cantidad_max(disponibles)
            if cantidad == 0:
                continue
            confirmar_reserva(pid, fid, cantidad)
        elif opcion == '3':
            mostrar_resumen_final()
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == '__main__':
    main()