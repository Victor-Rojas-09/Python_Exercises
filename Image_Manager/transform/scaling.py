import numpy as np


class ImageReduction:
    """
    Reduce la resolución de la imagen
    """

    def apply(self, img: np.ndarray, factor: int) -> np.ndarray:

        if factor <= 0:
            raise ValueError("El factor debe ser mayor que 0")

        return img[::factor, ::factor]


class ImageAmplification:
    """
    Amploa una región central de la imagen mediante
    repeticion de píxeles.
    """

    def apply(self, img: np.ndarray, zoom_area: int, zoom_factor: int = 5) -> np.ndarray:

        h, w = img.shape[:2]

        start_row = h // 2 - zoom_area // 2
        end_row = h // 2 + zoom_area // 2

        start_col = w // 2 - zoom_area // 2
        end_col = w // 2 + zoom_area // 2

        recorte = img[start_row:end_row, start_col:end_col]

        if img.ndim == 3:
            zoomed = np.kron(recorte, np.ones((zoom_factor, zoom_factor, 1)))
        else:
            zoomed = np.kron(recorte, np.ones((zoom_factor, zoom_factor)))

        return zoomed.astype(img.dtype)