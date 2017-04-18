# Input
n = int(input("n: "))

total = 0                   # iniciando acumulador
while n > 0:
    total += (n % 10)       # actualizando acumulador
    n //= 10                # actualizando digito inicial

print(total)
