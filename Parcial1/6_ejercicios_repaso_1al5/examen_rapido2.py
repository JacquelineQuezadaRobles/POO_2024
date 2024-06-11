
basico= 0,987
intermedio= 1.203 
consumo= 1

print(input(float("Ingrese la cantidad de kWh consumidas: ")))
while consumo <= 150:
    multi=basico*consumo
    iva= multi*0.10
    total= iva + 12.56
    print(f"Total a pagar: {total}")

while consumo >= 150:
    multi=intermedio*consumo
    iva= multi*0.10
    total= iva + 12.56
    print(f"Total a pagar: {total}")