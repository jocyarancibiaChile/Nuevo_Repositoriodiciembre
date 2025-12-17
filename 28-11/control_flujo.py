
pin_correcto = "1234"
intentos=3

while intentos >0:
    pin_ingresado= input("ingrese su pin: ")

    if pin_ingresado == pin_correcto:
        print(f"bienvenido")
        break
    else:
        intentos-= 1
        print(f"pin incorrecto intente nuevamente")
    
    if intentos == 0:
        print("cuenta bloqueada, comuníquese con el banco.")