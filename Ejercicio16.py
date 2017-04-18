# Input
n = int(input("n: "))

anterior = 0
siguiente = 1
i = 2
if n == 1:
    print(0)
else:
    print('0 1 ', end='')
    while i < n:
        aux = anterior + siguiente
        print(aux, '', end='')
        anterior, siguiente = siguiente, aux
        i += 1
