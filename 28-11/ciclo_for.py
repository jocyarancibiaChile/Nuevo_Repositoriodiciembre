
ciudades_objetivo=['paris','madrid','berlin','rancagua','talca','concepción', 'valparaiso','valdivia']

for ciudad in ciudades_objetivo:
    print(f"La ciudad objetivo será: {ciudad}")

#enumerate nos entrega una Tupla (indice, valor)

for indice,ciudad in enumerate(ciudades_objetivo, start=1):
    print(f"{indice}.-La ciudad objetivo será:{ciudad}")

#para imprimir dos ciudades de la lista
print(ciudades_objetivo[3]+"-"+ciudades_objetivo[5])

#uso del range con 1 parámetro
for indice in range(5):
    print(f"el valor del indice es: {indice}")

#uso del range con 2 parámetros
for indice in range(1,5):
    print(f"el valor del indice es: {indice}")

print("===============")
#uso del range con 3 parámetros
indice_inicial=1
limite_superior=10
paso=2
for indice in range(indice_inicial, limite_superior, paso):
    print(f"el valor del indice es: {indice}")