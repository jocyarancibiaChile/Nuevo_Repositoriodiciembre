texto= "   Hola, me llamo Aureliano y me gusta Python!!   "

#1.- Quitar espacios sobrantes al principio y al final
print(f"|{texto.strip()}|")

#2.- Convertir todo a minúsculas
print(f"{texto.lower()}")

#3.- Reemplazar Aurelino por su nombre
nuevo_nombre=texto.replace("Aureliano","Jocelyne")
print(nuevo_nombre)

#4.- Verificar si el texto termina con "Python!!"
termina = texto.endswith("Python!!   ")
print (termina)

#5.- Dividir el texto en palabras y mostras cuantas tiene
palabras = texto.split()
print(palabras)
print(len(palabras))


#inicio:fin:paso

texto="python"
print(texto[0:3])

print(texto[-3:]) #resultado hon
print(texto[-3]) #solo la h

print(texto[::-1]) #muestra todo el nombre al revés nohtyp
print(texto[::2]) # de 2 en 2, muestra pto

numeros=[10,20,30,40,50]
print(numeros[1:4])
print(numeros[::2])
print(numeros[::-1])

palabra="desarrollador"
lista_numeros=[1,2,3,4,5,6,7,8]

#los primeros 5 caracteres de la palabra
#los últimos 4 caracteres de la palabra
#la palabra invertida
#los números en posición PAR
#los números de 3 al 6(inclusive)

print(palabra[0:6])
print(palabra[-4:])
print(palabra[::-1])
print(lista_numeros[1::2])
print(lista_numeros[2:6])