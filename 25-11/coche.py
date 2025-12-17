
class Coche:
    def __init__(self,p_marca,p_modelo,p_year,p_color):
        self.marca=p_marca
        self.modelo=p_modelo
        self.year=p_year
        self.color=p_color
    def detalles (self):
        print(f"marca:{self.marca}, modelo:{self.modelo}, año: {self.year}, color: {self.color}")
#metodo especial nos permite usar el metodo print para ver los valores de los atributos del objeto
    def __str__(self):
        return f"marca:{self.marca}, modelo:{self.modelo}, año: {self.year}, color: {self.color}"
    
marca=input("Ingrese la marca: ")
modelo=input("Ingrese el modelo: ")
year=input("Ingrese el year: ")
color=input("Ingrese el color: ")

auto1=Coche(marca, modelo, year, color)
if (year >=2022):
    print("es un coche nuevo")
else:
    print("es un coche viejo")

    

salir="nok"

while():
    print("elija una opción")
    print("a) modificar marca")
    print("b)modificar modelo")
    print("c) modificar año")
    print("d) modificar color")
    print("e) salir")
    opcion=input("ingrese su selección")
    if opcion == "a":
        pass
        #instrucciones para modificar marca
    elif opcion == "b":
        pass
    elif opcion == "c":
        pass
    elif opcion == "d":
        pass
    elif opcion == "e":
        break
    else:
        print("opcion no válida")
        continue

    #auto1.detalles ()

    print(auto1)