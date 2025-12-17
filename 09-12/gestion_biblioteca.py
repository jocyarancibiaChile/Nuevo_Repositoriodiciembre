
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
def menu():
    print("1: Libros disponibles: ")
    print("2: Buscar Libros según género: ")
    print("3: Contabilizar libros (Counter): ")
    print("4: Libros con stock menor a 3: ")
    print("5: Agregar nuevo libro y Actualizar stock: ")
    print("6: Eliminar libro por código: ")


def get_codigo():
    id_libro=input("El código del libro:").upper()
    if id_libro in libros:
        return id_libro
    else:
        print("Libro no existe!")
        return False
    
def siguiente_libro(libros): # B001
    lista_llave=list(libros.keys())
    ultima_llave=lista_llave[-1] 
    prefijo=ultima_llave[0] 
    numero=int(ultima_llave[1:]) 
    siguiente_numero=numero+1
    return f"{prefijo}{siguiente_numero:03d}"

contador=0
while True:
    menu()
    opcion=input("Ingrese una opción:")
    
    if opcion=="0":
        print("Gracias por usar nuestro sistema")
        break

    #Agregar un nuevo libro al diccionario
    elif opcion=="1":
        def mostrar_libros():
            print("\n📚 LISTA DE LIBROS")
            for codigo, datos in libros.items():
                print(f"{codigo}: {datos['titulo']} - {datos['autor'][0]} ({datos['genero']}) | Stock: {datos['stock']}")
        mostrar_libros()

    elif opcion=="2":
        
        def buscar_por_genero():
            genero = input("\n🔎 Ingresa un género para buscar: ").strip()
            generos = {datos["genero"] for datos in libros.values()}  # uso de set

            if genero not in generos:
                print("⚠ No hay libros de ese género.")
            return
        print(f"Libros del género '{genero}':")
        for codigo, datos in libros.items():
           if datos["genero"].lower() == genero.lower():
            print(f"- {datos['titulo']} ({datos['autor'][0]})")





        print("Ingrese los datos del nuevo libro")
        new_libro=input("Ingrese el Título del libro, autor, gérero y stock, separado por coma:")
        nuevo_libro=list(new_libro.split(","))
        
        nuevo_cod=siguiente_libro(libros)

                # como la llave no existe la crea, pero si existe la actualiza
        try:
            libros[nuevo_cod]={
                "titulo":nuevo_libro[0],
                "autor":(nuevo_libro[1]),
                "genero":(nuevo_libro[2]),
                "stock": int(nuevo_libro[3])
                }
        except ValueError as e:
            print("Debe ingresar un número:",e)
        except IndexError as e:
            print("Debe ingresar 3 elementos:",e)
        
    elif opcion=="2": #modificar stock
            # pedir el id libro -> id_libro
        id_libro=get_codigo()
        if id_libro:
                #pedir el nuevo stock
                    try:
                        nuevo_stock=int(input("Ingrese el nuevo stock:"))
                        libros[id_libro]["stock"] =nuevo_stock
                    except:
                        print("stock incorrecto")
                            
        elif opcion=="3":
        #eliminar libro
        # pedir el id libro -> id_libro
                id_libro=get_codigo()
                if id_libro:
                    libros.pop(id_libro)

        elif opcion=="4":
                #ver libros
                
            for id_libro,libros in libros.items():
                    print(f"Libros :{id_libro}")
                    print(f"Título:{libros["titulo"]}")
                    print(f"Autor:{libros["autor","fecha"]}")
                    print(f"Género:{libros["genero"]}")
                    print(f"Stock:{libros["stokc"]}")
                    print("--------------------")
        elif opcion=="5":
                # mostrar libross con stock <10
            for id_libro,libros in libros.items():
                if libros["stock"] <10:
                    print(f"Libros :{id_libro}")
                    print(f"Título:{libros["titulo"]}")
                    print(f"Autor:{libros["autor","fecha"]}")
                    print(f"Género:{libros["genero"]}")
                    print(f"Stock:{libros["stokc"]}")
                    print("--------------------")
             
        elif opcion=="6":
                id_libro=get_codigo()
                if id_libro:
                    print(f"^Los datos del libros son {libros[id_libro]}")
                    contador +=1

        print(f"Usted consultó {contador} veces ")
        


