NUM1 = int(input("Dame un numero:"))
NUM2 = int(input("Dame otro numero:"))
NUM3 = int(input("Dame otro numero:"))

if NUM1 > NUM2 and NUM1 > NUM3:
    print(f"{NUM1} es el numero mayor.")
if NUM2 > NUM1 and NUM2 > NUM3:
    print(f"{NUM2} es el numero mayor.")
if NUM3 > NUM1 and NUM3 > NUM2:
    print(f"{NUM3} es el numero mayor.")

print("Fin del programa.")

print("Otra solucion")
if NUM1 != NUM2 and NUM1 != NUM1 and NUM2 != NUM3:
    if NUM1 > NUM2 and NUM1 > NUM3:
        print(NUM1, "es el mayor")
    else:
        if NUM2 > NUM1 and NUM2 > NUM3:
            print(NUM2, "es el mayor")
        else:
            print(NUM3, "es el mayor")

print("La mis pero simplificada:")
if NUM1 != NUM2 and NUM1 != NUM3 and NUM2 != NUM3:
    if NUM1 > NUM2 and NUM1 > NUM3:
        print(NUM1, "es el mayor")
    else:
        if NUM2 > NUM1 and NUM2 > NUM3:
            print(NUM2, "es el mayor")
        else:
            print(NUM3, "es el mayor")



