import numpy as np


class Ejercicio06:
    def ejecutar(self, img):
        capa = np.copy(img)
        capa[:, :, 0] = 0
        capa[:, :, 1] = 0
        return capa