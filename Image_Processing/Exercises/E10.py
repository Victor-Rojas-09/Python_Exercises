import numpy as np


class Ejercicio10:
    def ejecutar(self, canal_r, canal_g, canal_b):

        img = np.zeros((canal_r.shape[0], canal_r.shape[1], 3))
        img[:, :, 0] = canal_r[:, :, 0]
        img[:, :, 1] = canal_g[:, :, 1]
        img[:, :, 2] = canal_b[:, :, 2]
        return img