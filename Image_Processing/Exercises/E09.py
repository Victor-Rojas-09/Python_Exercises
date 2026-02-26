import numpy as np


class Ejercicio09:
    def ejecutar(self, img):
        capa = np.copy(img)
        capa[:, :, 2] = 0
        return capa