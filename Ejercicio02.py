# OPCIONAL: para ir practicando operaciones con strings
titulo = "Datos para generar una tabla de conversion de Grados Farenheit a Grados Celsius"
print(titulo)
print('-'*len(titulo))
print()

# Inputs
limInf = int(input("Ingrese Limite inferior (grados F): "))
limSup = int(input("Ingrese Limite inferior (grados F): "))
print()

# while
f = limInf              #Iniciando contador
while f <= limSup:
    c = (f-32)*5/9
    print (f, c)
    f += 1              #Incrementando contador

# OPCIONAL: Si se desea explicar formato de print
# while con formato

# Imprimiendo cabecera
print()
print("RESULTADO CON FORMATO")
print ("{:10s} {:10s}".format("Farenheit", "Celsius"))

f = limInf              #Iniciando contador
while f <= limSup:
    c = (f-32)*5/9
    print ("{:10d} {:10.2f}".format(f, c))
    f += 1              #Incrementando contador
