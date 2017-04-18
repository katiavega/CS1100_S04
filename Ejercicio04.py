N = 7  # Segun la guia de estilos de programacion de Python (PEP 8), las constantes deben expresarse en mayusculas

# while
total = 0                       # iniciando acumulador
i = 1                           # iniciando contador
while i <= N:
    nota = float(input("Ingrese la nota "+str(i + 1)+" :"))

    # OPCIONAL: Usando formato
    # nota = float(input("Ingrese la nota {} :".format(i + 1)))

    total += nota;              # actualizando acumulador
    i += 1                      # incrementando contador

# Presentando promedio
print("El promedio es:", total / N)  # mostrar operaciones en print

# OPCIONAL: Usando formato
print("El promedio es: {:5.2f}".format(total / N))  # mostrar operaciones en print
