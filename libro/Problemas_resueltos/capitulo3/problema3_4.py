NOM = 0
SUE = float(input("Introduzca el sueldo del trabajador:"))
while (SUE != -1):
    if SUE < 1000:
        NSUE = SUE * 1.15
    else:
        NSUE = SUE * 1.12
    NOM = NOM + NSUE
    print(f"Tu nuevo sueldo es {NSUE}.")
    SUE = float(input("¿Hay otro sueldo?:"))
print(f"El acumulado de los nuevos sueldos de los trabajadores es de {NOM}.")
print("Fin del programa!!")
