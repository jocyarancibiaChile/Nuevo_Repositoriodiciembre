from collections import defaultdict, Counter

pares={x:x**2 for x in range(5)}
lista_pares=[x**2 for x in range(5)]

print(pares)
print(lista_pares)

#generador
def numero():
    yield "a"
    yield "b"
    yield "c"

for x in numero():
    print(f" llamada:{x}")

colores = ['rojo','azul','rojo','verde','verde','verde','rojo']

frecuencia={}

for color in colores:
    if color in frecuencia:
        frecuencia[color] +=1
    else:
        frecuencia[color]=1

print(frecuencia)

frec = defaultdict(int)

# si voy a un hotel y pido una habitacion que NO EXISTE, me tiran para afuera
# con defaultdict, si pido una habitacion que NO EXISTE, la construyen

for color in colores:
    frec[color] +=1

print(frec)
# Counter nos genera un diccionario con la frecuencia de los valores
conteo=Counter(colores)
# {'rojo': 3 , 'azul': 1 , 'verde': 3}
for color,cant in conteo.items():
    print(f"Color {color}:{cant}")

# most_common recibe como parametro la cantidad de resultados a entregar

print(f"El valor más frecuente es:{conteo.most_common(1)}")

usuarios={
    "usuario1":{"nombre":"Ana","edad":25},
    "usuario2":{"nombre":"Luis",
                "edad":30,
                "direcciones":
                    {"direccion1":"Alameda 1425",
                     "direccion2":"San diego 45"
                     }
                },
}

print(f"Edad del usuario 2:{usuarios["usuario2"]["edad"]}")
print(f"Direccion 2 del usuario 2:{usuarios["usuario2"]["direcciones"]["direccion2"]}")