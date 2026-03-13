import numpy as np


class RGBReconstructor:
    """
    Reconstruye una imagen RGB a partir de tres canales
    rojo, verde y azul.
    """

    def apply(self, r: np.ndarray, g: np.ndarray, b: np.ndarray) -> np.ndarray:

        if r.shape != g.shape or r.shape != b.shape:
            raise ValueError("All channels must be the same size.")

        h, w = r.shape[:2]

        img = np.zeros((h, w, 3), dtype=r.dtype)

        img[:, :, 0] = r[:, :, 0]
        img[:, :, 1] = g[:, :, 1]
        img[:, :, 2] = b[:, :, 2]

        return img