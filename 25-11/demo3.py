edad= int(input("ingrese su edad"))

if(edad < 0):
    print(f"es válido")
elif(edad <=12):
    print(f"es un niño o niña")
elif(edad <=17):
    print(f"es un adolecente")
elif(edad <=64):
    print(f"es un adulto")
else:
    print(f"es adulto mayor")
    