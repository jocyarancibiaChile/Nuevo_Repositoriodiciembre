
# los objetos van a poseer dos miembros:
# 1. los atributos
# 2. los métodos  == ACCIONES QUE PUEDE REALIZAR EL OBJETO

class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    # los métodos que son de INSTANCIA deben tener como primer parámetro "self"
    def saludar(self):
        print(f"Hola mi nombre es{self.nombre} y mi edad es {self.edad}")

# primero vamos a INSTANCIAR LA CLASE == crear un objeto de la clase        

persona1= Persona("Pedro", 32)

persona1.saludar()

