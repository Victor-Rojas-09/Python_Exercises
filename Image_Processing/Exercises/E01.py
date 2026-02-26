import numpy as np
import matplotlib.pyplot as plt


class Ejercicio01:
    def ejecutar(self):
        img = np.zeros((3, 3, 3), dtype=np.uint8)

        img[0, 0] = [0, 255, 255]     # Cian
        img[0, 1] = [255, 255, 255]   # Blanco
        img[0, 2] = [255, 0, 0]       # Rojo

        img[1, 0] = [255, 0, 255]     # Magenta
        img[1, 1] = [128, 128, 128]   # Gris
        img[1, 2] = [0, 255, 0]       # Verde

        img[2, 0] = [255, 255, 0]     # Amarillo
        img[2, 1] = [0, 0, 0]         # Negro
        img[2, 2] = [0, 0, 255]       # Azul

        plt.imshow(img)
        plt.axis("off")
        plt.title("Ejercicio 01")
        plt.show()