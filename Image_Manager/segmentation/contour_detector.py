import cv2
import numpy as np

from Image_Manager.segmentation.threshold import ImageBinarization


class ContourDetector:
    """
    Detecta contornos en una imagen binaria.
    """

    def apply(
        self,
        img: np.ndarray,
        threshold: int = None,
        draw: bool = True
    ):
        """
        Detecta contornos en la imagen.
        """

        # Convertir a escala de grises si es necesario
        if img.ndim == 3:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        else:
            gray = img.copy()

        # Si se proporciona threshold, binarizar
        if threshold is not None:
            binarizer = ImageBinarization()
            binary = binarizer.apply(gray, threshold)
        else:
            binary = gray

        # Encontrar contornos
        contours, _ = cv2.findContours(
            binary,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        output_img = None

        if draw:
            # Convertir a color para dibujar
            if img.ndim == 2:
                output_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            else:
                output_img = img.copy()

            cv2.drawContours(output_img, contours, -1, (0, 255, 0), 2)

        return contours, output_img