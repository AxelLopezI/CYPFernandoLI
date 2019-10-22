ARSU = 0
ARNO = 0
MERSU = 50000
MES = 0
ARCE = 0
for I in range(1,13,1):
    print(f"Mes {I}:")
    RNO = float(input(f"Introduzca la lluvia caida en la region norte en el mes:"))
    RCE = float(input(f"Introduzca la lluvia caida en la region centro en el mes:"))
    RSU = float(input(f"Introduzca la lluvia caida en la region sur en el mes:"))

    ARNO += RNO
    ARCE += RCE
    ARSU += RSU

    if RSU < MERSU:
        MERSU = RSU
        MES = I
PRORCE = ARCE / 12
print(f"Promedio region centro:{PRORCE}")
print(f"Mes con menor lluvia en region sur:{MES}")
print(f"Registro del mes con menor lluvia es:{MERSU}")

if ARNO > ARCE:
    if ARNO > ARSU:
        print("La region con mayor lluvia es la region del norte.")
    else:
        print("La region con mayor lluvia es la region sur.")
elif ARCE > ARSU:
    print("La region con mayor lluvia es la region centro.")
else:
    print("La region con mayor lluvia es la region sur.")
    
print("Fin del programa!!")
