# Agenda simple

class Agenda:

    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def mostrar_contactos(self):
        print("\nContactos registrados:")
        for nombre, telefono in self.contactos.items():
            print(f"{nombre}: {telefono}")

    def consultar_contacto(self, nombre):
        if nombre in self.contactos:
            print(f"Teléfono de {nombre}: {self.contactos[nombre]}")
        else:
            print(f"No se encontró el contacto {nombre}.")


agenda = Agenda()

for i in range(3):
    nombre = input(f"Ingrese el nombre del contacto {i + 1}: ")
    telefono = input(f"Ingrese el teléfono de {nombre}: ")
    agenda.agregar_contacto(nombre, telefono)

agenda.mostrar_contactos()

nombre_consulta = input("\nIngrese el nombre del contacto a consultar: ")
agenda.consultar_contacto(nombre_consulta)
