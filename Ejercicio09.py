# Input
n = int(input("n: "))

# Validacion - No forma parte del algoritmo de factorial
if (n < 0):
    print("numero invalido")
    exit()

# Calculo de factorial
if n == 0:
    f = 1           # El scope de esta variable es global por lo cual puede ser usado en el bloque "padre"
else:
    i = 1
    f = 1
    while i <= n:
        f *= i
        i += 1

# Presentando factorial
print("el factorial es: ", f)
