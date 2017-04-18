# Input
multiplo = int(input("multiplo: "))
limite = int(input("limite: "))

i = 0                                   # iniciando contador
while multiplo*i <= limite:
    print(multiplo*i, " ", end='')      # imprimiendo en la misma linea usando parametro end=''
    i += 1                              # incrementando contador
