# Año bisiesto

class Anio:

    def __init__(self, valor):
        self.valor = valor

    def es_valido(self):
        return self.valor > 0

    def es_bisiesto(self):
        return (self.valor % 4 == 0 and self.valor % 100 != 0) or (self.valor % 400 == 0)


anio_ingresado = int(input("Ingrese un año: "))
anio = Anio(anio_ingresado)

if anio.es_valido():
    if anio.es_bisiesto():
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")
else:
    print("Año inválido. Debe ser mayor que 0.")
