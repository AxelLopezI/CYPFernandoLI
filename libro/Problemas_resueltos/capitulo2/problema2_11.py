CLAVE = int(input("Introduzca la clave de la zona geográfica a la que se llamó:"))
NUMIN = int(input("Introduzca la duración (en minutos) de la llamada:"))
if CLAVE == 12:
    COST = NUMIN*2
elif CLAVE == 15:
    COST = NUMIN*2.2
elif CLAVE == 18:
    COST = NUMIN*4.5
elif CLAVE == 19:
    COST = NUMIN*3.5
elif CLAVE == 23:
    COST = NUMIN*6
elif CLAVE == 25:
    COST = NUMIN*6
elif CLAVE == 29:
    COST = NUMIN*5
print("Costo total de la llamada", COST)
