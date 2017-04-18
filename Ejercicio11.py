# Input
n = int(input("n: "))

i = 1                       # Iniciando contador
while i <= n:
    if n % i == 0:
        print(i, " ", end="")
    i += 1                  # Incrementando contador
