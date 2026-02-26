import numpy as np


class Ejercicio07:
    def ejecutar(self, img):
        capa = np.copy(img)
        capa[:, :, 1] = 0
        return capa