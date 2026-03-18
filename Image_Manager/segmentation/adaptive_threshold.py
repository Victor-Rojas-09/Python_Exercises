import cv2
import numpy as np


class AdaptiveThreshold:
    """
    Aplica umbralización adaptativa para segmentación de la imagen.
    """

    def apply(
        self,
        img: np.ndarray,
        block_size: int,
        C: int,
        method: str = "gaussian"
    ) -> np.ndarray:
        """
        Aplica threshold adaptativo.
        """

        # Convertir a escala de grises si es necesario
        if img.ndim == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Asegurar que block_size sea impar
        if block_size % 2 == 0:
            block_size += 1

        if method == "mean":
            adaptive_method = cv2.ADAPTIVE_THRESH_MEAN_C
        else:
            adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C

        binary = cv2.adaptiveThreshold(
            img,
            255,
            adaptive_method,
            cv2.THRESH_BINARY,
            block_size,
            C
        )

        return binary