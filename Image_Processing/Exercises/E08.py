import numpy as np


class Ejercicio08:
    def ejecutar(self, img):
        capa = np.copy(img)
        capa[:, :, 0] = 0
        return capa