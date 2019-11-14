# arreglos
# lectura
# escritura / Asignación
# actualización : inserción, eliminación, modificación
# ordenamiento
# busqueda

# escritura
frutas = ["Zapote", "Manzana", "Pera", "Aguacate", "Durazno", "Uva", "Sandía"]

# lectura, el selector [indice]
print(frutas[2])
# lectura con for
# for option 1
for indice in range(0,7,1):
    print(frutas[indice])
print("-----")

# for opcion 2 -- por un iterador for each

for fr in frutas:
    print(fr)
    
# asignacion
frutas[2]="Melon"
print(frutas)


# inserción al final
frutas.append("Naranja")
print(frutas)
print(len(frutas))
frutas.insert(2,"Limón")
print(frutas)
print(len(frutas))
frutas.insert(0,"Mamey")
print(frutas)
# eliminación con pop
print(frutas.pop())
print(frutas)
print(frutas.pop(1))
print(frutas)
frutas[2]="Limón"
frutas.append("Limón")
frutas.append("Limón")
print(frutas)
frutas.remove("Limón")

#ordenamiento
frutas.sort()
print(frutas)
frutas.reverse()
print(frutas)

# busqueda
print(f"La Uva está en la posición { frutas.index('Uva')}")
print(f"El Limón está {frutas.count('Limón')} veces en la lista")

# concatenar
print(frutas)
otras_frutas = ["Rambutan","Nispero","Liche","Pitaya"]
frutas.extend(otras_frutas)
print(frutas)

# copiar

copia=frutas
copia.append("Naranja")
print(frutas)
print(copia)

otra_copia = frutas.copy()
otra_copia.append("Fresa")
otra_copia.append("Fresa")
print(frutas)
print(otra_copia)

















