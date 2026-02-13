# Numero en Rango

try:
    numero = int(input("Digite un número: "))

    if (numero >= 10) and (numero <= 20):
        print("Está entre 10 y 20.")
    else:
        print("Está fuera del rango.")

except ValueError:
    print("Debe ingresar un número válido.")