"""
Existe una estructura de condición llamada "if"
la cual evalua una condición para encontrar el valor "True" y si se cumple 
la condición se ejecuta la linea o las lineas de código. 

Tiene 4 variantes el if

"""

#Ejemplo_1 if simple

color=input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")

#Ejemplo_2 if compuesto

color=input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo_3 if anidado

color=input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("No soy el color rojo")
else:
    print("No soy el color rojo soy otra cosa")

#Ejemplo_4 if y elif

color=input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")
elif color=="azul":
    print("Soy el color azul")
elif color=="morado":
    print("Soy el color morado")

print("No soy ninguno de los anteriores")

#Ejemplo_5 Crear un programa que solicite el número de la semana e imprimir en pantalla el día que le corresponde.

numero=int(input("Ingrese el número de día (1 al 7)"))

if numero=="1":
    print("Domingo")
elif numero=="2":
    print("Lunes")
elif numero=="3":
    print("Martes")
elif numero=="4":
    print("Miercoles")
elif numero=="5":
    print("Jueves")
elif numero=="6":
    print("viernes")
elif numero=="7":
    print("Sabado")

else:
    print("No corresponde a ningun dia de la semana")








