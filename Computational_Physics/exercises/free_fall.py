import math

class FreeFall:
    g = 9.81

    @staticmethod
    def calculate_time(height: float) -> float:
        if height < 0:
            raise ValueError("La altura debe ser positiva.")
        return math.sqrt((2 * height) / FreeFall.g)
