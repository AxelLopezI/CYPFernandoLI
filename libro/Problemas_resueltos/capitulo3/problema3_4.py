NOM = 0
SUE = float(input("Introduzca el sueldo del trabajador:"))
while SUE != -1:
    if SUE < 1000:
        NSUE = SUE * 1.15
    else:
        NSUE = SUE * 1.12
    NOM += NSUE
    print(f"El nuevo sueldo del trabajador es de {NSUE}.")
    SUE = float(input("Introduzca el sueldo del trabajador:"))
print(f"El acumulado de los nuevos sueldos de los trabajadores es de {NOM}.")
print(f"Fin del programa!!")
