# Input
n = int(input("Ingrese los numeros de terminos: "))
a = float(input("Ingrese el valor de a: "))
x = float(input("Ingrese el valor de x: "))
y = float(input("Ingrese el valor de y: "))

#iniciando acumuladores
c = 0                  # coeficiente
ca = 0                  # coeficiente de a
suma = 0

i = 0                                       # iniciando contador
while i < n:

    c += 3
    ca = 2**i
    signo = (-1)**(i+1)                     # OJO: el operador ** tiene mayor precedencia que el operador -
                                            #      por ello el parentesis (-1)

    if i % 2:
        termino = signo * c*y / (ca*a**i)
    else:
        termino = signo * c*x / (ca*a**i)

    suma += termino
    i += 1                                  # incrementando contador

print(suma)
