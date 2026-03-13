import numpy as np


class GrayscaleAverage:
    """
    Convierte una imagen a escala de grises usando
    el metodo de promedio (Average).
    """

    def apply(self, img: np.ndarray) -> np.ndarray:

        gray = np.mean(img, axis=2)

        return np.stack((gray, gray, gray), axis=2)


class GrayscaleLuminosity:
    """
    Convierte una imagen a escala de grises usando
    el metodo de luminosidad.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:

        gray = (
            0.21 * img[:, :, 0] +
            0.72 * img[:, :, 1] +
            0.07 * img[:, :, 2]
        )

        return np.stack((gray, gray, gray), axis=2)


class GrayscaleMidgray:
    """
    Convierte una imagen a escala de grises usando
    el metodo Midgray.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        gray = (np.max(img, axis=2) + np.min(img, axis=2)) / 2

        return np.stack((gray, gray, gray), axis=2)