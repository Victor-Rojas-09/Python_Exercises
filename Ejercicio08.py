# Suma acumulada

suma = 0
cantidad = 0

while True:
    numero = float(input("Ingrese un número (0 para terminar): "))
    if numero == 0:
        break
    suma += numero
    cantidad += 1

if cantidad > 0:
    promedio = suma / cantidad
    print(f"Suma total: {suma}")
    print(f"Cantidad de números ingresados: {cantidad}")
    print(f"Promedio: {promedio}")
else:
    print("No se ingresaron números.")
