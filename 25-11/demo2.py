
numero= int(input("ingrese un numero entero"))

if(numero%2==0 and numero % 3 == 0):
    print(f" es par y múltiplo de 3")
elif(numero%2==0):
    print(f"es par pero no múltiplo de 3")
elif(numero%2!=0 and numero %3 == 0):
    print(f"es impar pero múltiplo de 3")
else:
    print(f"el numero es impar y no multiplo de 3")
    