import numpy as np


class Ejercicio12:
    def ejecutar(self, img):
        gris = np.mean(img, axis=2)
        return np.stack((gris, gris, gris), axis=2)