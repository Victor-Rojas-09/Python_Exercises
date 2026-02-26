import numpy as np


class Ejercicio05:
    def ejecutar(self, img):
        capa = np.copy(img)
        capa[:, :, 0] = 0
        capa[:, :, 2] = 0
        return capa