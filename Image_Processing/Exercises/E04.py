import numpy as np


class Ejercicio04:
    def ejecutar(self, img):

        capa = np.copy(img)
        capa[:, :, 1] = 0
        capa[:, :, 2] = 0
        return capa