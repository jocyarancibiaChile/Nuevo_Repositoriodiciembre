from collections import Counter

# Diccionario principal con libros registrados
libros = {
    "B001": {
        "titulo": "Cien años de soledad",
        "autor": ("Gabriel García Márquez", 1927),
        "genero": "Novela",
        "stock": 3
    },
    "B002": {
        "titulo": "El Principito",
        "autor": ("Antoine de Saint-Exupéry", 1900),
        "genero": "Fábula",
        "stock": 5
    },
    "B003": {
        "titulo": "Python para todos",
        "autor": ("Charles Severance", 1950),
        "genero": "Educativo",
        "stock": 2
    },
    "B004": {
        "titulo": "It",
        "autor": ("Stephen King", 1947),
        "genero": "Terror",
        "stock": 4
    }
}

# Menú

def menu():
    print("\n MENÚ DE OPCIONES")
    print("1: Mostrar libros disponibles")
    print("2: Buscar libros según género")
    print("3: Contabilizar libros por género (Counter)")
    print("4: Libros con stock menor a 3")
    print("5: Agregar nuevo libro")
    print("6: Actualizar stock de un libro")
    print("7: Eliminar libro por código")
    print("0: Salir")

def get_codigo():
    id_libro = input("Ingrese el código del libro: ").upper()
    if id_libro in libros:
        return id_libro
    else:
        print("Libro no existe.")
        return None

def siguiente_libro():
    lista_llave = list(libros.keys())
    ultima_llave = lista_llave[-1]  # último código
    prefijo = ultima_llave[0]
    numero = int(ultima_llave[1:])
    siguiente_numero = numero + 1
    return f"{prefijo}{siguiente_numero:03d}"

#Mostrar libros
def mostrar_libros():
    print("\n LISTA DE LIBROS")
    for codigo, datos in libros.items():
        print(f"{codigo}: {datos['titulo']} - {datos['autor'][0]} ({datos['genero']}) | Stock: {datos['stock']}")

#Buscar por género
def buscar_por_genero():
    genero = input("\n Ingresa un género para buscar: ").strip()
    encontrados = [datos for datos in libros.values() if datos["genero"].lower() == genero.lower()]
    if encontrados:
        print(f"\n Libros del género '{genero}':")
        for libro in encontrados:
            print(f"- {libro['titulo']} ({libro['autor'][0]})")
    else:
        print(" No hay libros de ese género.")

#contabilizar libros 
def contabilizar_libros():
    generos = [datos["genero"] for datos in libros.values()]
    contador = Counter(generos)
    print("\n Cantidad de libros por género:")
    for genero, cantidad in contador.items():
        print(f"- {genero}: {cantidad}")

#Libros con stock menor a 3
def libros_bajo_stock():
    print("\n Libros con stock menor a 3:")
    for codigo, datos in libros.items():
        if datos["stock"] < 3:
            print(f"{codigo}: {datos['titulo']} | Stock: {datos['stock']}")

#Agregar nuevo libro
def agregar_libro():
    print("\n Ingrese los datos del nuevo libro")
    try:
        titulo = input("Título: ")
        autor = input("Autor: ")
        anio = int(input("Año de edidición del libro: "))
        genero = input("Género: ")
        stock = int(input("Stock inicial: "))
        nuevo_cod = siguiente_libro()
        libros[nuevo_cod] = {
            "titulo": titulo,
            "autor": (autor, anio),
            "genero": genero,
            "stock": stock
        }
        print(f" Libro '{titulo}' agregado con código {nuevo_cod}.")
    except ValueError:
        print(" Error: año y stock deben ser números enteros.")

#Actualizar stock
def actualizar_stock():
    id_libro = get_codigo()
    if id_libro:
        try:
            nuevo_stock = int(input("Ingrese el nuevo stock: "))
            libros[id_libro]["stock"] = nuevo_stock
            print(f" Stock actualizado: {libros[id_libro]['titulo']} ahora tiene {nuevo_stock} unidades.")
        except ValueError:
            print(" Stock inválido, debe ser un número entero.")
#Eliminar libro
def eliminar_libro():
    id_libro = get_codigo()
    if id_libro:
        eliminado = libros.pop(id_libro)
        print(f" Libro '{eliminado['titulo']}' eliminado correctamente.")



contador = 0
while True:
    menu()
    opcion = input("\nIngrese una opción: ")

    if opcion == "0":
        print(" Gracias por usar nuestro sistema.")
        break
    elif opcion == "1":
        mostrar_libros()
    elif opcion == "2":
        buscar_por_genero()
        contador += 1
    elif opcion == "3":
        contabilizar_libros()
    elif opcion == "4":
        libros_bajo_stock()
    elif opcion == "5":
        agregar_libro()
    elif opcion == "6":
        actualizar_stock()
    elif opcion == "7":
        eliminar_libro()
    else:
        print(" Opción inválida.")

    print(f"\n Usted ha consultado géneros {contador} veces.")