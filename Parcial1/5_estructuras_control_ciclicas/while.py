"""
Ciclo While es una Estructura iterativa que se ejecuta X veces siempre y 
cuando la condición se  

Sintaxis
 while condicion:
   bloque de instrucciones

"""

#Ejemplo_1 Crear un programa que imprima en pantalla 5 veces el @

contador=1
suma=0

while contador<=5:
     print("@")
     contador+=1

#Ejemplo_2 Crear un programa que imprima los números del 1 al 5 y los sume y al final imprima la suma.
    
contador=1
suma=0

while contador<=5:
    print(contador)
    suma+=contador
    contador+=1

print(f"La suma es: {suma}")


#Ejemplo_3 Crear un programa que imprima la tabla de multiplicar que el usuario desee.

tabla=int(input("Ingrese un numero para calcular su tabla de multiplicar: "))

i=1
multi=0

while i <=10:
    multi=i*tabla
    i+=1
    print(f"{tabla} X {i} = {multi}")
