import math

class Projectile:
    g = 9.81

    @staticmethod
    def max_range(v0: float, angle_deg: float) -> float:
        angle = math.radians(angle_deg)
        return (v0**2 * math.sin(2 * angle)) / Projectile.g

    @staticmethod
    def max_height(v0: float, angle_deg: float) -> float:
        angle = math.radians(angle_deg)
        return (v0**2 * math.sin(angle)**2) / (2 * Projectile.g)
