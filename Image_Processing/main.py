import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Importaciones
from Exercises.E01 import Ejercicio01
from Exercises.E02 import Ejercicio02
from Exercises.E03 import Ejercicio03
from Exercises.E04 import Ejercicio04
from Exercises.E05 import Ejercicio05
from Exercises.E06 import Ejercicio06
from Exercises.E07 import Ejercicio07
from Exercises.E08 import Ejercicio08
from Exercises.E09 import Ejercicio09
from Exercises.E10 import Ejercicio10
from Exercises.E11 import Ejercicio11
from Exercises.E12 import Ejercicio12
from Exercises.E13 import Ejercicio13
from Exercises.E14 import Ejercicio14

# Funciones generales 

def cargar_imagen(ruta):
    img = Image.open(ruta).convert("RGB")
    img = np.asarray(img, dtype=np.float32) / 255.0
    return img


def mostrar_imagen(img, titulo="Resultado"):
    plt.imshow(img)
    plt.axis("off")
    plt.title(titulo)
    plt.show()


# Menu de pruebas
def menu():
    print("\n-Opciones")
    print("01. Matriz de colores")
    print("02. Imagen desde matriz")
    print("03. Invertir colores")
    print("04. Canal rojo")
    print("05. Canal verde")
    print("06. Canal azul")
    print("07. Canal magenta")
    print("08. Canal cyan")
    print("09. Canal amarillo")
    print("10. Reconstruir imagen RGB")
    print("11. Fusionar imágenes")
    print("12. Escala de grises (Average)")
    print("13. Escala de grises (Luminosity)")
    print("14. Escala de grises (Midgray)")
    print("0. Salir")

while True:
    menu()
    opcion = input("\nSeleccione un ejercicio: ")

    if opcion == "0":
        print("Saliendo del programa...")
        break

    elif opcion == "1":
        Ejercicio01().ejecutar()

    elif opcion == "2":
        Ejercicio02().ejecutar()

    elif opcion in ["3", "4", "5", "6", "7", "8", "9", "12", "13", "14"]:
        ruta = input("Ingrese la ruta: ")
        img = cargar_imagen(ruta)

        ejercicios = {
            "3": Ejercicio03(),
            "4": Ejercicio04(),
            "5": Ejercicio05(),
            "6": Ejercicio06(),
            "7": Ejercicio07(),
            "8": Ejercicio08(),
            "9": Ejercicio09(),
            "12": Ejercicio12(),
            "13": Ejercicio13(),
            "14": Ejercicio14(),
        }

        resultado = ejercicios[opcion].ejecutar(img)
        mostrar_imagen(resultado, f"Ejercicio {opcion}")

    elif opcion == "10":
        r = cargar_imagen(input("Ruta imagen canal R: "))
        g = cargar_imagen(input("Ruta imagen canal G: "))
        b = cargar_imagen(input("Ruta imagen canal B: "))

        resultado = Ejercicio10().ejecutar(r, g, b)
        mostrar_imagen(resultado, "Reconstrucción RGB")

    elif opcion == "11":
        img1 = cargar_imagen(input("Ruta de la primera imagen: "))
        img2 = cargar_imagen(input("Ruta de la segunda imagen: "))

        resultado = Ejercicio11().ejecutar(img1, img2)
        mostrar_imagen(resultado, "Fusión de imágenes")

    else:

        print("Opción inválida. Intente nuevamente.")
