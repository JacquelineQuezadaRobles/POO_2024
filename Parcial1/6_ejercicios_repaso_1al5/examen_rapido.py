
print(input("Ingrese nombre del paciente: "))
print(input("Tipo de sangre: "))

contador=1

for contador in range (1,4):
    print(input("Ingrese los intervalos de presion arterial: "))


presion= 120

while presion <= 120:
    print("Presenta una presion normal")

while presion >= 130:
    print("Presenta una presion alta")

