# Funcion area

def area_triangulo(base, altura):
    return (base * altura) / 2


b = float(input("Ingrese la base del triángulo: "))
h = float(input("Ingrese la altura del triángulo: "))

area = area_triangulo(b, h)
print(f"El área del triángulo es: {area}")