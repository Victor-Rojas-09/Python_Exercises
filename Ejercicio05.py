# Clasificacion de nota

class Evaluacion:

    def __init__(self, nota):
        self.nota = nota

    def es_valida(self):
        return 0 <= self.nota <= 5

    def clasificar(self):
        if self.nota >= 4.5:
            return "Excelente"
        elif self.nota >= 3.5:
            return "Buena"
        elif self.nota >= 3.0:
            return "Aprobada"
        else:
            return "Reprobada"


nota = float(input("Ingrese una nota entre 0 y 5: "))
evaluacion = Evaluacion(nota)

if evaluacion.es_valida():
    print(evaluacion.clasificar())
else:
    print("Nota inválida. Debe estar entre 0 y 5.")
