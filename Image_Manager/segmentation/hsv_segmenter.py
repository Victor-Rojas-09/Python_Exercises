import cv2
import numpy as np


class HSVColorSegmenter:
    """
    Clase para realizar segmentación de colores en imágenes
    utilizando el espacio de color HSV.
    """

    def __init__(self, image_path: str):

        self.image_path = image_path
        self.image = cv2.imread(image_path)

        if self.image is None:
            raise ValueError(
                f"The image could not be loaded from the path.: {image_path}"
            )

        self.hsv_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)

    def create_mask(self, lower_color: tuple, upper_color: tuple) -> np.ndarray:
        """
        Crea una mascara binaria basada en un rango de color HSV.
        """

        lower = np.array(lower_color, dtype=np.uint8)
        upper = np.array(upper_color, dtype=np.uint8)

        mask = cv2.inRange(self.hsv_image, lower, upper)

        return mask

    def apply_mask(self, mask: np.ndarray) -> np.ndarray:
        """
        Aplica una mascara a la imagen original.
        """

        segmented = cv2.bitwise_and(self.image, self.image, mask=mask)

        return segmented