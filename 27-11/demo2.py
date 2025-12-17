
print("Bienvenido al asistente de tostadas")

hay_pan=input("hay pan disponible? (s/n):" )

if hay_pan=="n":
    print("No hay pan. No podemos hacer tostadas: ''(")
else:
    tostado=input("EL pan está tostado? (s/n): ")

    if tostado=="n":
        print("Tostando el pan...")

    mantequilla=input("Quiere ponerle mantequilla? (s/n):")

    if mantequilla=="s":
        print("Agregando mantequilla al pan tostado")
    print("Tostada lista para servir, disfrute su pan tostado")

print ("Gracias por usar el asistente!")