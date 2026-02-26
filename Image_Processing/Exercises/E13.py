import numpy as np


class Ejercicio13:
    def ejecutar(self, img):
        gris = 0.21 * img[:, :, 0] + 0.72 * img[:, :, 1] + 0.07 * img[:, :, 2]
        return np.stack((gris, gris, gris), axis=2)