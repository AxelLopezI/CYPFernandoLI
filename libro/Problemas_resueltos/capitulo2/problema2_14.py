TIPOENF = int(input("Introduzca el tipo de enfermedad del paciente:"))
EDAD = int(input("Introduzca la edad del paciente:"))
DIAS = int(input("Introduzca el número de días que el paciente estuvo hospitalizado:"))
if TIPOENF == 1:
    COSTOT = DIAS*25
elif TIPOENF == 2:
    COSTOT = DIAS*16
elif TIPOENF == 3:
    COSTOT = DIAS*20
elif TIPOENF == 4:
    COSTOT = DIAS*32
if EDAD >= 14:
    if EDAD <= 22:
        COSTOT = COSTOT*1.10
print(f"Costo total: ${COSTOT}")
print("Fin del programa!!")
