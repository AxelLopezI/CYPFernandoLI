MAT = int(input("Escriba la matrícula del alumno:"))
CAL1 = float(input("Escriba la calificación 1 del alumno { MAT }:"))
CAL2 = float(input("Escriba la calificación 2 del alumno { MAT }:"))
CAL3 = float(input("Escriba la calificación 3 del alumno { MAT }:"))
CAL4 = float(input("Escriba la calificación 4 del alumno { MAT }:"))
CAL5 = float(input("Escriba la calificación 5 del alumno { MAT }:"))
PRO = (CAL1 + CAL2 + CAL3 + CAL4 + CAL5) / 5
print(f"El promedio del alumno { MAT } es { PRO }.")
