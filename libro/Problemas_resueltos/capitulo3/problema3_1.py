SUMPAR = 0
SUMIMP = 0
CUEPAR = 0
I = 1
for I in range(1,271,1):
    NUM = int(input("Introduzca un numero entero:"))
    if NUM % 2 == 0:
        if (-1**NUM) > 0:
            SUMPAR += NUM
            CUEPAR += 1
    else:
        SUMIMP += NUM
    I += 1
PROPAR = SUMPAR/CUEPAR
print(f"{PROPAR}, {SUMIMP}")
print("Fin del programa!!")
