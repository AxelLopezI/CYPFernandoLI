#import Modulos
#Modulos.mi_print("Hola")

from Modulos import *
import time
import sys
from asciistuff import Banner

mi_print("Hola de nuevo")
otro_print("Otro print usado")
print(sumar(3 , 5))
print(restar(10 , 7))

for i in range (10 , 0 , -1):
    print( i  , "...")
    time.sleep(0.1) #Pausa "tantos" segundos
print(Banner("FELIZ ANO NUEVO"))

#print(sys.platform)

print(Banner("ICO FES ARAGON"))
