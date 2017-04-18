#Input
n = int(input("Ingrese un numero: "))

s = 0               # iniciando acumulador
i = 1               # iniciando contador
while (i <= n):      # evaluando condicion
    s += i          # actualizando acumular
    i += 1          # incrementando contador

# Imprimiendo Total
print("la suma total es:", s)

# OPCIONAL: Usando Formato
print("la suma total es: {:2}".format(s))


