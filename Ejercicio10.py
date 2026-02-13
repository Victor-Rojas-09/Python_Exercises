# Lista de notas

class RegistroNotas:

    def __init__(self):
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def nota_mayor(self):
        return max(self.notas) if self.notas else None

    def nota_menor(self):
        return min(self.notas) if self.notas else None

    def promedio(self):
        return sum(self.notas) / len(self.notas) if self.notas else None

    def mostrar_resultados(self):
        print(f"Lista de notas: {self.notas}")
        print(f"Nota mayor: {self.nota_mayor()}")
        print(f"Nota menor: {self.nota_menor()}")
        print(f"Promedio: {self.promedio():.2f}")


registro = RegistroNotas()

for i in range(5):
    nota = float(input(f"Ingrese la nota { i +1}: "))
    while nota < 0 or nota > 5:
        print("Nota inválida. Debe estar entre 0 y 5.")
        nota = float(input(f"Ingrese la nota { i +1}: "))
    registro.agregar_nota(nota)

registro.mostrar_resultados()