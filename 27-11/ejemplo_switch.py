

def obtener_dia(numero):
    dias = {
        1:"lunes",
        2:"martes",
        3:"miércoles",
        4:"jueves",
        5:"viernes",
        6:"sábado",
        7:"domingo"
    }
    return dias.get(numero, "un número inválido")

num=int(input("Ingrese un número (1-7):" ))
print(f"El día correpondiente es {obtener_dia(num)}")

    