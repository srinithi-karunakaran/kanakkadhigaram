"""
கட்டிட முழக்கோல் அளவுகள் (Building Measurement System)
=====================================================

பாடல்கள் 52-53 அடிப்படையில்
கட்டிடங்களின் முழக்கோல் அளவுகள்.

This module defines traditional Tamil architectural measurement
based on building types mentioned in Kanakkadhigaram.
"""

# ==========================================================
# DATA
# ==========================================================

BUILDING_MUZHAM = {
    "மனை": 24,
    "கோவில்": 25,
    "அமைச்சர் மனை": 26,
    "மன்னர் அரண்மனை": 27
}

# ==========================================================
# CORE FUNCTIONS
# ==========================================================

def list_buildings():
    """
    பாடல் 52
    இருபது நாலி னாலே முழமனை கோல தாகும்
    கருதிய இருபத் தஞ்சாம் கடவுளார் கோவி லுக்கு
    பெருகிய இருபத் தாராம் பெருந்திரு வமைச்சர் கோயில்
    மருவளர் மன்னர் கோவில் வளரிரு பத்தே மென்ப

    பாடல் 53
    இருபது மேலு நாலு விரல்மனை முழக்கோல் ஆகும்
    கருதிய இருபத் தைந்தாங் காணுநற் கோயில் எல்லாம்
    பெருகிய இருபத் தாராம் பெருந்திரு மன்னர் கோயில்
    வருந்திரு மடமான் அன்னாய் வழிகளும் இருபத் தேழே
    """
    return list(BUILDING_MUZHAM.keys())


def get_building_muzham(building):
    """Return size in muzham."""
    if building not in BUILDING_MUZHAM:
        raise ValueError(f"Unknown building: {building}")
    return BUILDING_MUZHAM[building]


def compare_buildings():
    return {
        b: f"{v} முழம்"
        for b, v in BUILDING_MUZHAM.items()
    }


def get_building_info(building):
    """Return full info dict."""
    return {
        "building": building,
        "muzham": get_building_muzham(building)
    }

# ==========================================================
# TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("BUILDINGS:", list_buildings())

    print("\nINDIVIDUAL:")
    for b in list_buildings():
        print(get_building_info(b))

    print("\nCOMPARISON:")
    print(compare_buildings())