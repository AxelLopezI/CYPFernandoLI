MAY = -100000
MEN = 100000
N = int(input("Introduzca el numero de enteros que se ingresan:"))
I = 1
for I in range(1,N,1):
    NUM = int(input("Introduzca el numero entero que se ingresa:"))
    if NUM > MAY:
        MAY = NUM
    else:
        if NUM < MEN:
            MEN = NUM
        else:
            I = I + 1
print(f"{MAY}, {MEN}")
print("Fin del programa!!")

