import cv2
import matplotlib.pyplot as plt
import numpy as np

from Image_Manager.color.channels import (
    ColorInverter,
    RedChannel,
    GreenChannel,
    BlueChannel,
    MagentaChannel,
    CyanChannel,
    YellowChannel
)
from Image_Manager.color.histogram import Histogram
from Image_Manager.color.reconstruction import RGBReconstructor
from Image_Manager.color.adjustments import BrightnessAdjust, ChannelAdjust
from Image_Manager.color.grayscale import (
    GrayscaleAverage,
    GrayscaleLuminosity,
    GrayscaleMidgray
)

from Image_Manager.transform.rotation import ImageRotator
from Image_Manager.transform.translation import ImageTranslation
from Image_Manager.transform.scaling import ImageReduction, ImageAmplification
from Image_Manager.transform.crop import ImageCrop
from Image_Manager.transform.blend import ImageBlendAverage

from Image_Manager.segmentation.threshold import ImageBinarization
from Image_Manager.segmentation.hsv_segmenter import HSVColorSegmenter


def show(title, img):

    if img.ndim == 3:
        img = cv2.cvtColor(img.astype(np.uint8), cv2.COLOR_BGR2RGB)

    plt.figure()
    plt.title(title)
    plt.imshow(img, cmap="gray")
    plt.axis("off")


def main():
    img1 = cv2.imread("../data/IMG01.jpg")
    img2 = cv2.imread("../data/IMG02.jpg")

    if img1 is None or img2 is None:
        raise ValueError("No se pudieron cargar las imágenes")

    show("Imagen 1", img1)
    show("Imagen 2", img2)

    # Invertir colores
    inverter = ColorInverter()
    inv_img = inverter.apply(img1)
    show("Invert Colors", inv_img)


    # Canales RGB
    red = RedChannel().apply(img1)
    green = GreenChannel().apply(img1)
    blue = BlueChannel().apply(img1)

    show("Red Channel", red)
    show("Green Channel", green)
    show("Blue Channel", blue)


    # Canales secundarios
    magenta = MagentaChannel().apply(img1)
    cyan = CyanChannel().apply(img1)
    yellow = YellowChannel().apply(img1)

    show("Magenta Channel", magenta)
    show("Cyan Channel", cyan)
    show("Yellow Channel", yellow)


    # Reconstrucción RGB
    reconstructor = RGBReconstructor()
    reconstructed = reconstructor.apply(red, green, blue)
    show("RGB Reconstruction", reconstructed)

    # Histograma del canal Rojo
    red_histogram = Histogram()
    red_histogram.applyRed(img1)
    # Histograma del canal Verde
    green_histogram = Histogram()
    green_histogram.applyGreen(img1)
    # Histograma del canal Azul
    blue_histogram = Histogram()
    blue_histogram.applyBlue(img1)

    # Ajuste de brillo
    brightness = BrightnessAdjust()
    bright_img = brightness.apply(img1, 50)
    show("Brightness +50", bright_img)


    # Ajuste de canal
    channel_adjust = ChannelAdjust()
    red_boost = channel_adjust.apply(img1, 0, 80)
    show("Increase Red Channel", red_boost)


    # Escala de grises
    gray_avg = GrayscaleAverage().apply(img1)
    gray_lum = GrayscaleLuminosity().apply(img1)
    gray_mid = GrayscaleMidgray().apply(img1)

    show("Grayscale Average", gray_avg)
    show("Grayscale Luminosity", gray_lum)
    show("Grayscale Midgray", gray_mid)


    # Reducción de imagen
    reducer = ImageReduction()
    reduced = reducer.apply(img1, 3)
    show("Image Reduction", reduced)


    # Zoom
    amplifier = ImageAmplification()
    zoom = amplifier.apply(img1, 100)
    show("Image Amplification", zoom)


    # Rotación
    rotator = ImageRotator()
    rotated = rotator.apply(img1, 45)
    show("Rotation 45°", rotated)


    # Traslación
    translator = ImageTranslation()
    translated = translator.apply(img1, 150, 100)
    show("Translation", translated)


    # Recorte
    cropper = ImageCrop()
    cropped = cropper.apply(img1, 100, 400, 100, 400)
    show("Crop", cropped)


    # Fusión de imágenes
    blender = ImageBlendAverage()
    blended = blender.apply(img1, img2)
    show("Image Blend Average", blended)


    # Binarización
    binarizer = ImageBinarization()
    binary = binarizer.apply(img1, 120)
    show("Binarization", binary)

    # Segmentación HSV
    segmenter = HSVColorSegmenter("../data/IMG01.jpg")

    # Valores para segmentar una mascara amarilla
    lower_yellow = (10, 110, 80)
    upper_yellow = (30, 255, 255)
    mask = segmenter.create_mask(lower_yellow, upper_yellow)
    segmented = segmenter.apply_mask(mask)

    show("HSV Mask", mask)
    show("HSV Segmentation", segmented)


    plt.show()


if __name__ == "__main__":
    main()