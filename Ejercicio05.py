# Input
n = int(input("Ingrese un numero: "))

# while
s = 0               # iniciando acumulador
i = 1               # iniciando contador
while i <= n:
    t = (2*i - 2)**2
    s += t          # actualizando acumulador
    i += 1          # actualizando contador

# Presentando sumatoria
print("La sumatoria es: ", s)
