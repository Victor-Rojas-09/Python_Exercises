import numpy as np


class ColorInverter:
    """
    Invierte los colores de una imagen RGB.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        """
        Invierte los colores de la imagen.
        """
        return 1 - img


class RedChannel:
    """
    Extrae unicamente el canal rojo de la imagen.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 0] = 0
        result[:, :, 1] = 0

        return result


class GreenChannel:
    """
    Extrae unicamente el canal verde de la imagen.
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
        result[:, :, 1] = 0
        result[:, :, 2] = 0
        return result


class MagentaChannel:
    """
    Extrae el canal magenta.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 1] = 0
        return result


class CyanChannel:
    """
    Extrae el canal cyan.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 2] = 0
        return result


class YellowChannel:
    """
    Extrae el canal amarillo.
    """

    def apply(self, img: np.ndarray) -> np.ndarray:
        result = np.copy(img)
        result[:, :, 0] = 0
        return result