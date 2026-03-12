import numpy as np


class ColorInverter:
    """
    Invierte los colores de una imagen RGB.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        """
        Invierte los colores de la imagen.

        Parameters
        ----------
        img : np.ndarray
            Imagen RGB con valores normalizados o en rango 0-255.

        Returns
        -------
        np.ndarray
            Imagen con colores invertidos.
        """
        return 1 - img


class RedChannel:
    """
    Extrae únicamente el canal rojo de la imagen.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 1] = 0
        result[:, :, 2] = 0
        return result


class GreenChannel:
    """
    Extrae únicamente el canal verde de la imagen.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 0] = 0
        result[:, :, 2] = 0
        return result


class BlueChannel:
    """
    Extrae únicamente el canal azul de la imagen.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 0] = 0
        result[:, :, 1] = 0
        return result


class MagentaChannel:
    """
    Genera el canal magenta (Rojo + Azul).
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 1] = 0
        return result


class CyanChannel:
    """
    Genera el canal cyan (Verde + Azul).
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 0] = 0
        return result


class YellowChannel:
    """
    Genera el canal amarillo (Rojo + Verde).
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 2] = 0
        return result