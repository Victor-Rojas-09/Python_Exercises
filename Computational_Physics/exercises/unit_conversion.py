class UnitConversion:

    @staticmethod
    def kmh_to_ms(speed: float) -> float:
        return speed / 3.6

    @staticmethod
    def ms_to_kmh(speed: float) -> float:
        return speed * 3.6
