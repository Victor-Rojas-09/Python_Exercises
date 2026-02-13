# Operaciones basicas

class Operaciones:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def suma(self):
        return self.a + self.b

    def resta(self):
        return self.a - self.b

    def multiplicacion(self):
        return self.a * self.b

    def division_entera(self):
        return self.a // self.b

    def division_real(self):
        return self.a / self.b

    def residuo(self):
        return self.a % self.b

    def potencia(self):
        return self.a ** self.b


a = int(input("Digite su primer número: "))
b = int(input("Digite su segundo número: "))

operaciones = Operaciones(a, b)

print("Suma:", operaciones.suma())
print("Resta:", operaciones.resta())
print("Multiplicación:", operaciones.multiplicacion())
print("División Entera:", operaciones.division_entera())
print("División Real:", operaciones.division_real())
print("Residuo:", operaciones.residuo())
print("Potencia:", operaciones.potencia())
