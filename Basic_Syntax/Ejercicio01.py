# Datos personales

class Persona:
    def __init__(self, nombre, edad, estatura, estudiante):
        self.nombre = nombre
        self.edad = edad
        self.estatura = estatura
        self.estudiante = estudiante

    def descripcion(self):
        return print(f"{self.nombre}, {self.edad} años, {self.estatura} m de estatura")

    def es_estudiante(self):
        return self.estudiante


nombre = input("Digita tu nombre: ")
edad = int(input("Digita tu edad: "))
estatura = float(input("Digita tu estatura (en metros): "))
estudiante_input = input("¿Eres estudiante? (si/no): ").lower()

estudiante = estudiante_input in ["si", "sí", "s"]

persona = Persona(nombre, edad, estatura, estudiante)

persona.descripcion()

if persona.es_estudiante():
    print("Es estudiante.")
else:
    print("No es estudiante")
