A = int(input("Introduzca un número entero:"))
B = int(input("Introduzca un número entero diferente al anterior:"))
C = int(input("Introduzca un número entero diferente a los anteriores:"))
if A < B:
    if B < C:
        print("Los numeros están en orden creciente.")
    else:
        print("Los números no están en orden creciente.")
else:
    print("Los números no están en orden creciente.")
print("Fin del programa!!")
