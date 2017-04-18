# Input
n = int(input("n: "))

# while
i = 0                       # Inicializando Contador i
while i < n:
    j = 0                   # Inicializando Contador j
    while j < i + 1:
        print('+', end='')
        j += 1              # Incrementando Contador j
    print()
    i += 1                  # Incrementando Contador i
