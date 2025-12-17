from registro import esta_registrado, registrar_usuario


nombre = input("Ingresa tu nombre:")
edad = input("Ingresa tu edad:")

if esta_registrado(nombre) :
    print(f"El usuario {nombre} está registrado.")
else :
    registrar_usuario(nombre, edad)
    print(f"El usuario {nombre} se registró exitosamente.")