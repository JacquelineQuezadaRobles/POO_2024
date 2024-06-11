"""
# Una funcion es un conjunto de instrucciones  agrupadas bajo un 
# nombre en particular coo un programa mas pequeño que cumple
# una funcion especifica. La funcion se puede reutilizar con el simple hecho de invocarla 
# es decir mandarla llamar

# sintaxis

# def NombreDeMiFuncion(parametros):
#     bloque o conjunto de instrucciones


# NombreDeMiFuncion

# Las funciones pueden ser de  4 tipos
# 1. Funcion que no recibe parametros y no regresa valor 
# 2. Funcion que no recibe parametros y regresa valor 
# 3. Funcion que recibe parametros y no regresa valor 
# 4. Funcion que recibe parametros y regresa valor
"""

    # 1. Funcion que no recibe parametros y no regresa valor 
 def sumaNumeros():
   
     sumaNumeros1()


# 2. Funcion que no recibe parametros y regresa valor
def sumaNumeros2():
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))
    suma=n1+2
    return f"{n1}+{n2}={suma}"

    print(sumaNumeros2())


# 3. Funcion que recibe parametros y no regresa valor
def sumaNumeros3(n1,n2):
    suma=n1+2
    return f"{n1}+{n2}={suma}"

n1=int(input("Numero # 1:"))
n2=int(input("Numero # 2:"))
sumaNumeros3(34,23)

# 4. Funcion que recibe parametros y regresa valor
def sumaNumeros4(n1,n2):
    suma=n1+2
    return f"{n1}+{n2}={suma}"

n1=int(input("Numero # 1:"))
n2=int(input("Numero # 2:"))
print(sumaNumeros4(n1,n2))


#Ejemlo 6. Crear un programa que solicite a traves de una función la siguiente 
# información: Nombre del paciente, Edad, Estatura, Tipo de sangre, utiliazar los 4 tipos de funciones.
