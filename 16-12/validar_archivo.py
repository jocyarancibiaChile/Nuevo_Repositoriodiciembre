from pathlib import Path
# bASE_DIR nos traerá la ruta ABSOLUTA de donde estamos ejecutando el programa
BASE_DIR = Path(__file__).resolve().parent

print(BASE_DIR)

archivo=BASE_DIR / "documentos/prueba.txt"

if archivo.exists():
    print("el archivo existe!")
    #Podemos abrir el archivo sin problema

else:
    print("el archivo no existe!")

