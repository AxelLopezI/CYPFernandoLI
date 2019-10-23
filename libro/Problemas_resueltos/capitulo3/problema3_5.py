SUMOTR = 0
SUMPOS = 0
CUEPOS = 0
N = int(input("Introduzca el numero de datos que serán ingresados:"))
I = 0
for I in range(1,N,1):
    NUM =int(input("Introduzca un numero entero:"))
    if NUM > 0:
        SUMPOS += NUM
        CUEPOS += 1
    else:
        SUMOTR += NUM
    I += 1
PROGEN = (SUMPOS + SUMOTR)/N
PROPOS = (SUMPOS/CUEPOS)
print(f"Hay {CUEPOS} numeros positivos.")
print(f"{PROPOS} es el promedio de los numeros positivos.")
print(f"{PROGEN} es el promedio general de los numeros.")
print(f"Fin del programa!!")
