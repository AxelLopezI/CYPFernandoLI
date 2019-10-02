A = float(input("Introduzca un valor diferente de 0:"))
B = float(input("Introduzca un valor:"))
C = float(input("Introduzca un valor:"))
DIS = B**2-4*A*C
if DIS >= 0:
    X1 = ((-B)+DIS**0.5)/2*A
    X2 = ((-B)-DIS**0.5)/2*A
    print(f"Sus raíces reales son {X1} y {X2}")
print("Fin del programa")
