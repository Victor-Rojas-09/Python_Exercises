import numpy as np


class Ejercicio11:
    def ejecutar(self, img1, img2):
        #Fusion

        h = min(img1.shape[0], img2.shape[0])
        w = min(img1.shape[1], img2.shape[1])

        img1_rec = img1[:h, :w]
        img2_rec = img2[:h, :w]

        return (img1_rec + img2_rec) / 2