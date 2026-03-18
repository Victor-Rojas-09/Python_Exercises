import cv2
import numpy as np


class Erosion:
    """
    Aplica erosión morfológica para reducir regiones blancas en una imagen.
    """

    def apply(self, img: np.ndarray, kernel_size: int = 3, iterations: int = 1) -> np.ndarray:
        """
        Aplica erosión a la imagen.
        """

        kernel = np.ones((kernel_size, kernel_size), np.uint8)

        eroded = cv2.erode(img, kernel, iterations=iterations)

        return eroded