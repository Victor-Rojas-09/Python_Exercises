import cv2
import numpy as np


class GaussianBlur:
    """
    Aplica un suavizado gaussiano a la imagen para reducir ruido.
    """

    def apply(self, img: np.ndarray, ksize: int) -> np.ndarray:
        """
        Aplica desenfoque gaussiano.
        """

        # Asegurar que el kernel sea impar
        if ksize % 2 == 0:
            ksize += 1

        blurred = cv2.GaussianBlur(img, (ksize, ksize), 0)

        return blurred