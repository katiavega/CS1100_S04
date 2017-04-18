# Input
b = int(input("Ingrese la base: "))
e = int(input("Ingrese el exponente: "))

# while
p = 1               # iniciando acumulador
i = 1               # iniciando contador
while i <= e:
    p *= b          # actualizando acumulador
    i += 1          # incrementando contador

# Presentando el resultado de la potencia
print("La potencia es:", p)
