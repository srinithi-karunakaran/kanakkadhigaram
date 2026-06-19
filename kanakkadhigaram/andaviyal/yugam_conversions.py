"""
யுக காலக் கணக்கீடு (Yuga Cosmology System)
==========================================

கணக்கதிகாரம் அடிப்படையில் யுக கால அளவுகளை கணக்கிடும் தொகுதி.

இதில் உள்ளவை:
- கிரேதா, திரேதா, துவாபர, கலி யுகங்கள்
- சதுர்யுக கணக்கீடு
- அடிப்படை 216000 multiplication system

------------------------------------------------------------
This module implements the Yuga time system from "Kanakkadhigaram".

"""

# ==========================================================
# BASE SYSTEM (VERSE 39)
# ==========================================================

YUGA_BASE_VALUE = 216000

YUGA_FACTORS = {
    "கிரேதாயுகம்": 8,
    "திரேதாயுகம்": 6,
    "துவாபரயுகம்": 4,
    "கலியுகம்": 2
}

# ==========================================================
# CORE CLASS
# ==========================================================

class YugaSystem:
    """
    பாடல் 40:
    இருநாற் றொருபதி னாயி ரத்தை
    இருதா லிருமூன்றின் நாவில் - நிருமித்த
    பின்னிரண்டு தன்னில் பெருக்கில் திருமாதே!
    நன்னுமொடு நாலுகத்தின் சீர்.

    Parameters
    ----------
    base_value : int
        அடிப்படை வருட அளவு (default = 216000)

    Methods
    -------
    get_yuga(name)
        குறிப்பிட்ட யுகத்தின் வருட எண்ணிக்கை

    get_all()
        அனைத்து யுகங்களின் மதிப்புகள்

    get_chaturyuga()
        4 யுகங்களின் மொத்தம்
    """

    def __init__(self, base_value=YUGA_BASE_VALUE):
        self.base_value = base_value

    def get_yuga(self, name: str) -> int:
        if name not in YUGA_FACTORS:
            raise ValueError(f"தெரியாத யுகம்: {name}")
        return self.base_value * YUGA_FACTORS[name]

    def get_all(self):
        return {
            k: self.base_value * v
            for k, v in YUGA_FACTORS.items()
        }

    def get_chaturyuga(self):
        return sum(self.get_all().values())

    def convert(self, value, from_yuga, to_yuga):
        if from_yuga not in YUGA_FACTORS or to_yuga not in YUGA_FACTORS:
            raise ValueError("தெரியாத யுகம்")

        base = value * self.get_yuga(from_yuga)
        return base / self.get_yuga(to_yuga)


# ==========================================================
# SIMPLE TEST
# ==========================================================

if __name__ == "__main__":
    system = YugaSystem()

    print("=== ALL YUGAS ===")
    print(system.get_all())

    print("\n=== CHATURE YUGA ===")
    print(system.get_chaturyuga())

    print("\n=== TEST ===")
    print(system.convert(1, "கிரேதாயுகம்", "கலியுகம்"))