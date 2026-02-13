class Displacement:

    @staticmethod
    def calculate(u: float, a: float, t: float) -> float:
        return (u * t) + (0.5 * a * (t**2))
