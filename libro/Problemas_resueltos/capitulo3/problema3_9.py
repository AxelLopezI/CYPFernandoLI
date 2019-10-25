SERIE = 0
N = int(input("Introduzca el número de términos de la serie:"))
I = 1
for I in range(1,N,1):
    SERIE = SERIE + I**I
    I +=1
    print("La serie es:", SERIE)
print("Fin del programa!!")
