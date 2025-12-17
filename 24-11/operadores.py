#operadores aritmeticos
# parra convertir un tipo de dato (str) a otro (int) se usa el método int

try:
#try nos sirve para intentar realizar una acción "peligrosa" para el programa.
   ok=0
    primero =int(input("Ingrese el primero número: "))
    segundo =int(input("Ingrese el segundo número: "))

    print(f"La suma de los números es {primero+segundo}")
    print(f"La resta de los números es {primero-segundo}")
    print(f"La multiplicacion de los números es {primero*segundo}")
    print(f"La division de los números es {primero/segundo}")
    print(f"El resto de la division de los números es {primero%segundo}")
    
except ZeroDivisionError
    print(f"esta dividiendo por cero: ")
except:
    print("Usted ha ingresado un valor que no es un número")
ok=1

# OPERADORES DE COMPARACION
if(primero > segundo):
    print("el primero es mayor")
elif(primero<segundo):
    print("el segundo es mayor")
else:
    print("son iguales")

#OPERADORES LOGICOS
if (ok==1 and primero >18):
    print("todo bien y mayir de edad")
elif(ok==0 or primero >18):
    print("problema o pero mayor a 18")
else:
    print("estamos con problema")