SUE = float(input("Introduzca el sueldo del trabajador:"))
if SUE < 1000:
    AUM = SUE * 0.15
    NSUE = SUE + AUM
    print(f"El nuevo sueldo es ${NSUE}.")
print("Fin del programa.")
