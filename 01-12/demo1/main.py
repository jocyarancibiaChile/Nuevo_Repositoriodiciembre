from modulos.operaciones import sumar

opcion=input("Elija que quiere sumar: (s)String o (e)Enteros: ")

if opcion == "s":
    str1 = input("ingrese el primer String: ")
    str2 = input("ingrese el segundo String: ")
    print(f"La suma de los strings es: {sumar(str1,str2)}")
elif opcion == "e":
    num1 = int(input("Ingrese el primer número ENTERO: "))
    num2 = int(input("Ingrese el segundo número ENTERO: "))
    print(f"La suma de los números es: {sumar(num1,num2)}")
