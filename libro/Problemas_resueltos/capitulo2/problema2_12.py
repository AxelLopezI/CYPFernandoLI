SUE = float(input("Introduzca el sueldo básico del trabajador:"))
CATE = int(input("Introduzca la categoría de trabajador (1 a 8):"))
HE = int(input("Introduzca las horas extra trabajadas por el trabajador:"))
if CATE == 1:
    PHE = 30
elif CATE == 2:
    PHE = 38
elif CATE == 3:
    PHE = 50
elif CATE == 4:
    PHE = 70
elif CATE > 4:
    PHE = 0
if HE > 30:
    NSUE = SUE + 30*PHE
else:
    NSUE = SUE + HE*PHE
print(f"${NSUE}")
