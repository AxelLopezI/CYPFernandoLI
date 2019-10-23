SUMSER = 0
I = 2
BAND = 'T'
while (I <= 1800):
    SUMSER += 1
    print(f"El incremento del valor es {I}.")
    if BAND == 'T':
        BAND = 'F'
        I += 3
    else:
        BAND = 'T'
        I += 2
print(f"Los terminos son {SUMSER}.")
print("Fin del programa!!")
