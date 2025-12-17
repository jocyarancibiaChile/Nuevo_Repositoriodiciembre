usuarios_registrados={}

usuarios_registrados


def registrar_usuario(nombre,edad):
    usuarios_registrados[nombre]=edad
    return True

def esta_registrado(nombre):
    if nombre in usuarios_registrados:
        return True
    else:
        return False