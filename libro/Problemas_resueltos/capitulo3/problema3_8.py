NUM = int(input("Introduzca el numero:"))
if NUM > 0:
    while (NUM != 1):
        print(f"El numero es {NUM}.")
        if (-1 ** NUM) > 0:
            NUM = NUM/2
        else:
            NUM = (NUM*3) + 1
        print(f"El numero es {NUM}.")
        NUM = int(input("Ingresa un número:"))
else:
    print(f"El numero que se ingresa debe ser entero positivo, {NUM} no es una entrada válida.")
print("Fin del programa!!")
