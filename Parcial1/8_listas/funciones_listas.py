paises=["México","USA","Brasil","China"]
numeros=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

#Ordenar las listas
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

print(varios)
varios.sort()
print(varios)

#Agregar elemmentos a la lista
print(numeros)
numeros.append(100)
print(numeros)
numeros.insert(len(numeros),200)
print(numeros)

#Remover elementos
print(numeros)
numeros.remove(100)
print(numeros)
numeros.pop(2)
print(numeros)


#Remover elementos

varios.reverse()
print(varios)

#Buscar un valor dentro de una lista.

encontro="Brasil" in paises
print(encontro)

#Vaciar una lista
print(paises)
paises.clear()
print(encontro)


#Unir listas 
print(varios)
varios.extend(numeros)
print(varios)


