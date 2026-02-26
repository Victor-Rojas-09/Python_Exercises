import numpy as np


class Ejercicio14:
    def ejecutar(self, img):
        gris = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
        return np.stack((gris, gris, gris), axis=2)