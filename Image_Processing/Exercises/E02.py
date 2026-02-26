import numpy as np
import matplotlib.pyplot as plt


class Ejercicio02:
    def ejecutar(self):
        grad = np.linspace(0, 1, 11)
        img = np.zeros((7, 12, 3))
        color = np.array([1, 1, 1])

        for i in range(11):
            img[:, i, :] = (1 - grad[i]) * color + grad[i] * np.array([0, 0, 0])

        colores = [
            ([1, 1, 0], 0, 2),
            ([0, 1, 1], 2, 4),
            ([0, 1, 0], 4, 6),
            ([1, 0, 1], 6, 8),
            ([1, 0, 0], 8, 10),
            ([0, 0, 1], 10, 12),
        ]

        for color, c1, c2 in colores:
            img[0:5, c1:c2] = color

        plt.imshow(img)
        plt.axis("off")
        plt.title("Ejercicio 02")
        plt.show()