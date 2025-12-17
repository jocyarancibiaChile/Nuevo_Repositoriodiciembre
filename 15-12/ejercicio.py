'''
Ejercicio:

1.- Leer un archivo de texto con los datos de usuarios
2.- validar cada registro usando try/except
3.- Construir una lista de usuarios válidos
4.- Escribir los usuarios válidos en un archivo nuevo
5.- Escribir los usuarios inválidos en un archivo de errores

'''

def validar_usuario(linea):
     #Ana;25;ana@ejemplo.com 
    partes=linea.strip().split(";") #lista de 3 elementos 0,1,2
    if len(partes)!=3:
         raise ValueError("Formato incorrecto, no vienen 3 campos.")
    nombre=partes[0]
    edad=partes[1]
    correo=partes[2]
#validar nombre
    if len(nombre.strip())<2:
         raise ValueError("Nombre muy corto")
#validar la edad
    try:
         edad=int(edad)
    except ValueError as e:
         raise ValueError ("Edad no es un número entero")
    
    if edad<0 or edad >120:
         raise ValueError("Edad fuera del rango normal (0-120)")
    
#Validad el correo
    if "@" not in correo or "." not in correo:
         raise ValueError ("Correo no válido") 
         
    return {"nombre": nombre, "edad": edad, "email": correo}

def procesar_archivo():
    usuario_valido=[]
    errores=[]

    try: 
        with open("usuarios_raw.txt","w",encoding="utf-8") as archivo:
            lineas=archivo.readlines()
            for linea in lineas:
                try:
                    usuario=validar_usuario(linea)
                    usuario_valido.append(usuario)
                except Exception as e:
                    errores.append(linea)
                    
    except FileNotFoundError as e:
        print("Archivo no encontrado")
    else:
        print("Archivo procesado correctamente")
    finally:
        print("Fin de la lectura del archivo")
                
    with open("nuevo_archivo.txt","w",encoding="uft-8") as f1:
        for usuario in usuario_valido:
            f1.write(f"{usuario["nombre"]};{usuario["edad"]};{usuario["email"]}\n")

    with open("errores.txt","a",encoding="uft-8") as f2:
        for error in errores:
            f2.write(error)

    print("Termino del procesamiento")
    print(f"Lineas con usuarios válidados{len(usuario_valido)}")
    print(f"Lineas con errores válidados{len(errores)}")
