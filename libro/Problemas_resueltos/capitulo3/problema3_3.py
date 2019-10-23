SERIE = 0
N = int(input("Introduzca el numero que representa los terminos de la serie:"))
BAND = 'T'
I = 1
for I in range(1,N,1):
    if BAND == 'T':
        SERIE = SERIE + 1/I
        BAND = 'F'
    else:
        SERIE = SERIE - 1/I
        BAND = 'T'
    I = I + 1
print(f"El resultado de dicha serie es {SERIE}")
print("Fin del programa!!")
