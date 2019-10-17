MAT = int(input("Introduzca la matrícula del alumno:"))
CARR = str(input("Introduzca la carrera en la que está inscrito el alumno:"))
SEM = int(input("Introduzca el semestre que tiene aprobado el alumno:"))
PROM = float(input("Introduzca el promedio del alumno:"))
if CARR == "Economia":
    if SEM >= 6:
        if PROM >= 8.8:
            print(f"{MAT}, {CARR}, Aceptado.")
elif CARR == "Computacion":
    if SEM >= 6:
        if PROM >= 8.5:
            print(f"{MAT}, {CARR}, Aceptado.")
elif CARR == "Aministracion":
    if SEM >= 5:
        if PROM >= 8.5:
            print(f"{MAT}, {CARR}, Aceptado.")
elif CARR == "Contabilidad":
    if SEM >= 5:
        if PROM >= 8.5:
            print(f"{MAT}, {CARR}, Aceptado.")
print("Fin del programa!!")


