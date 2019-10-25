MED = 0
CHI = 0
GRA = 0
N = int(input("Introduzca el numero de ventas:"))
I = 1
for I in range(1,N,1):
    V = float(input("Introduzca la venta del vendedor:"))
    if V <= 200:
        CHI = CHI + 1
    else:
        if V < 400:
            MED = MED + 1
        else:
            GRA = GRA + 1
    I = I + 1
print(f"{CHI}, {MED}, {GRA} ")
print("Fin del programa!!")
