import math

class Vectors:

    @staticmethod
    def add(v1: list, v2: list) -> list:
        if len(v1) != len(v2):
            raise ValueError("Los vectores deben tener la misma dimension.")
        return [v1[i] + v2[i] for i in range(len(v1))]

    @staticmethod
    def dot_product(v1: list, v2: list) -> float:
        return sum(v1[i] * v2[i] for i in range(len(v1)))

    @staticmethod
    def angle(v1: list, v2: list) -> float:
        dot = Vectors.dot_product(v1, v2)
        mag1 = math.sqrt(sum(x**2 for x in v1))
        mag2 = math.sqrt(sum(x**2 for x in v2))
        return math.degrees(math.acos(dot / (mag1 * mag2)))
