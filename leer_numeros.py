numeros1 = archivo.read()
print(numeros1)
print(numeros1.split('\n'))
print(numeros1.split())
lista_num = []
for linea in numeros1.split('\n'):
    for numero in linea.split(','):
print(f"El mayor es :{lista_num[-1]} y el menor es:{lista_num[0]}")
archivo.close()

lista_num = []
for linea in numeros1.split():
    for numero in linea.split(','):
        lista_num.append(int(numero))
print(lista_num)
lista_num.sort()
print(f"Lista ordenada:{lista_num}")
print(f"El mayor es :{lista_num[-1]} y el menor es:{lista_num[0]}")
archivo.close()

archivo=open("numeros.txt","rt")
numero2 = archivo.readlines()
print(numero2)

print(numero2)
archivo.close()

archivo=open("numeros.txt","rt")
lista_num = archivo.readlines()
print(lista_num)
archivo.close()


