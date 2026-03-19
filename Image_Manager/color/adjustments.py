import numpy as np


class BrightnessAdjust:
    """
    Class for adjusting the brightness of an image.
    """

    def apply(self, img: np.ndarray, value: int) -> np.ndarray:

        imgf = img.astype(np.int32)

        result = np.clip(imgf + value, 0, 255)

        return result.astype(np.uint8)


class ChannelAdjust:
    """
    Adjusts the brightness of a specific channel in the image.
    """

    def apply(self, img: np.ndarray, channel: int, value: int) -> np.ndarray:

        if channel not in [0, 1, 2]:
            raise ValueError("The channel must be 0 (R), 1 (G), or 2 (B).")

        result = img.astype(np.int32).copy()

        result[:, :, channel] = np.clip(
            result[:, :, channel] + value,
            0,
            255
        )

        return result.astype(np.uint8)