import numpy as np


class ImageBinarization:
    """
    Convierte una imagen a binaria utilizando un umbral
    aplicado sobre su version en escala de grises.
    """

    def apply(self, img: np.ndarray, threshold: int) -> np.ndarray:

        gray = (
            0.21 * img[:, :, 0] +
            0.72 * img[:, :, 1] +
            0.07 * img[:, :, 2]
        )

        binary = np.where(gray > threshold, 255, 0)

        return binary.astype(np.uint8)