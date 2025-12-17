
'''SISTEMA DE GESTION DE BIBLIOTECA'''

# Registro inicial de libros

libros = {
    "L001": {
        "titulo": "Cien años de soledad",
        "anio_edicion": 1967,
        "autor": "Gabriel García Márquez",
        "stock": 5,
        "genero": "Novela",
        "arrendatario": None,
        "tiempo_arriendo": 0,
        "multa": 0
    },
    "L002": {
        "titulo": "El Principito",
        "anio_edicion": 1900,
        "autor": "Antoine de Saint-Exupéry",
        "stock": 10,
        "genero": "Fábula",
        "arrendatario": None,
        "tiempo_arriendo": 0,
        "multa": 0
    },
    "L003": {
        "titulo": "Python para todos",
        "anio_edicion": 1950,
        "autor": "Charles Severance",
        "stock": 5,
        "genero": "Educativo",
        "arrendatario": None,
        "tiempo_arriendo": 0,
        "multa": 0
    },

    "L004": {
        "titulo": "It",
        "anio_edicion": 1947,
        "autor": "Stephen King",
        "genero": "Terror",
        "stock": 4,
        "arrendatario": None,          
        "tiempo_arriendo": 0,
        "multa": 0, 
    },

    "L005": {
        "titulo": "Don Quijote de la Mancha",
        "anio_edicion": 1605/1615,
        "autor": "Cervantes",
        "genero": "Novela/Parodia",
        "stock": 10,
        "arrendatario": None,          
        "tiempo_arriendo": 0,
        "multa": 0 
    },

    "L006": {
        "titulo": "Frankenstein",
        "anio_edicion": 1818,
        "autor": "Shelley",
        "genero": "Gótico/Ciencia",
        "stock": 5,
        "arrendatario": None,          
        "tiempo_arriendo": 0,
        "multa": 0 
    },

    "L007": {
        "titulo": "Crimen y castigo",
        "anio_edicion": 1866,
        "autor": "Dostoyevski",
        "genero": "Realismo Psicológico",
        "stock": 4,
        "arrendatario": None,          
        "tiempo_arriendo": 0,
        "multa": 0 
    },

    "L008": {
        "titulo": "Orgullo y prejuicio",
        "anio_edicion": 1813,
        "autor": "Austen",
        "genero": "Romance/realismo",
        "stock": 8,
        "arrendatario": None,          
        "tiempo_arriendo": 0,
        "multa": 0 
    },

    "L009": {
        "titulo": "1984",
        "anio_edicion": 1949,
        "autor": "George Orwell",
        "genero": "Distopía, Ciencia Ficción Política",
        "stock": 5,
        "arrendatario": None,          
        "tiempo_arriendo": 0,
        "multa": 0 
    },

    "L010": {
        "titulo": "El extranjero",
        "anio_edicion": 1942,
        "autor": "Albert Camus",
        "genero": "Existencialismo, Novela Filosófica",
        "stock": 7,
        "arrendatario": None,          
        "tiempo_arriendo": 0,
        "multa": 0 
    },
}

#Menú
def menu():
    print("MENÚ DEL SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("1: Libros disponibles")
    print("2: Buscar libro por ID")
    print("3: Contabilizar consultas")
    print("4: Libros con stock menor a 3")
    print("5: Registrar nuevo libro")
    print("6: Eliminar libro por código")
    print("7: Arriendo de libro")
    print("8: Multa por atraso")
    print("9: Devolución de libro")
    print("0: Salir")

# Funciones
def get_codigo():
    id_libro = input("El código del libro: ").upper()
    if id_libro in libros:
        return id_libro
    else:
        print("Libro no existe!")
        return None

def mostrar_libros():
    print("Libros disponibles:")
    for codigo, datos in libros.items():
        print(f"{codigo} | {datos['titulo']} ({datos['anio_edicion']}) | "
              f"Autor: {datos['autor']} | Género: {datos['genero']} | Stock: {datos['stock']}")

def buscar_por_id():
    id_libro = get_codigo()
    if id_libro:
        datos = libros[id_libro]
        print(f"Libro encontrado: {datos['titulo']} ({datos['anio_edicion']}) - {datos['autor']}")

def registrar_libro():
    nuevo_id = input("Ingrese código del libro: ").upper()
    if nuevo_id in libros:
        print("El ID ya existe.")
        return
    titulo = input("Título: ")
    anio = int(input("Año de edición: "))
    autor = input("Autor: ")
    genero = input("Género: ")
    stock = int(input("Cantidad disponible: "))

    libros[nuevo_id] = {
        "titulo": titulo,
        "anio_edicion": anio,
        "autor": autor,
        "genero": genero,
        "stock": stock,
        "arrendatario": None,
        "tiempo_arriendo": 0,
        "multa": 0
    }
    print(f"Libro '{titulo}' registrado correctamente.")

def eliminar_libro():
    id_libro = get_codigo()
    if not id_libro:
        print("Código inválido.")
        return
    
    libro = libros.get(id_libro)
    if not libro:
        print("El libro no existe.")
        return
    
    confirm = input(f"¿Está seguro de eliminar el libro '{libro['titulo']}'? (s/n): ").lower()
    if confirm == "s":
           
        libros.pop(id_libro)
        print(f"Libro {libro['titulo']},' eliminado." f"Quedan {libro['stock']} ejemplares.") 
    
    else:
        print("Operación cancelada")


def arrendar_libro():
    id_libro = get_codigo()
    if not id_libro:
        print ("Código inválido")
        return

    persona = input("Nombre del arrendatario: ").strip()
    rut=input("Ingrese el rut: ").strip()

    try:
        tiempo = int(input("Tiempo de arriendo (días): "))
        if tiempo <=0:
            print("El tiempo de arriendo debe ser mayor a 0.")
            return
    except ValueError:
        print("Debe ingresar un número válido para el tiempo de arriendo.")
        return


    fecha_salida = input("Ingrese la fecha de salida (DD/MM/AAAA): ").strip()
    
    tiempo_maximo = 7
    valor_dia = 300

    libro = libros.get(id_libro)
    if not libro :
        print ("El libro no existe.")
        return

    if libro["stock"] > 0:
        libro["arrendatario"] = persona
        libro["rut"] = rut
        libro["tiempo_arriendo"] = tiempo
        libro["fecha de salida"]= fecha_salida
        libro["stock"] -= 1
        libro["multa"] = max(0, (tiempo - tiempo_maximo)* valor_dia)
           
        print(f"Libro '{libro['titulo']}' arrendado por {persona,rut})."f"fecha de salida {fecha_salida}."f"Multa: ${libro['multa']}")
    else:
            print("No hay stock disponible.")

def devolver_libro():
    id_libro = get_codigo()
    if id_libro:
        libro = libros[id_libro]
        if libro["arrendatario"]:
            print(f"Devolución de '{libro['titulo']}' por {libro['arrendatario']}. Multa: ${libro['multa']}")
            libro["stock"] += 1
            libro["arrendatario"] = None
            libro["tiempo_arriendo"] = 0
            libro["multa"] = 0
        else:
            print("Ese libro no está arrendado.")

def libros_bajo_stock():
    print("Libros con stock menor a 3:")
    for codigo, datos in libros.items():
        if datos["stock"] < 3:
            print(f"{codigo} | {datos['titulo']} | Stock: {datos['stock']}")

# Programa principal
contador = 0
while True:
    menu()
    opcion = input("Ingrese una opción: ")

    if opcion == "0":
        print("Gracias por usar nuestro sistema")
        break
    elif opcion == "1":
        mostrar_libros()
    elif opcion == "2":
        buscar_por_id()
        contador += 1
        print(f"Consultas realizadas: {contador}")
    elif opcion == "3":
        print(f" Usted ha consultado {contador} veces.")
    elif opcion == "4":
        libros_bajo_stock()
    elif opcion == "5":
        registrar_libro()
    elif opcion == "6":
        eliminar_libro()
    elif opcion == "7":
        arrendar_libro()
    elif opcion == "8":
        print("La multa se calcula automáticamente al arrendar libros con exceso de tiempo.")
    elif opcion == "9":
        devolver_libro()
    else:
        print(" Opción inválida.")
