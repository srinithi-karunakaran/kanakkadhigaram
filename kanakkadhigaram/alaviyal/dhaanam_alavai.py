"""
தான அளவீட்டு முறை (Donation Scaling System)
==========================================

Ancient Tamil mathematical system from Kanakkadhigaram (பாடல் 82).

This module includes:
- Multi-level donation classification (24 types)
- Fractional scaling system
- Cross-unit mapping between volume, grain, and value systems
"""

# ==========================================================
# 1. BASE DONATION STRUCTURE (VERSE 82)
# ==========================================================

DONATION_GROUPS = {
    "நிலவாய்": 5,
    "நெல்வாய்": 7,
    "நீர்வாய்": 12
}

# ==========================================================
# 2. FRACTIONAL LAND SYSTEM
# ==========================================================

LAND_FRACTIONS = [
    1/320,
    1/160,
    1/80,
    1/20,
    1/4
]

# ==========================================================
# 3. GRAIN / VOLUME SYSTEM
# ==========================================================

GRAIN_UNITS = {
    "செவிடு": 1,
    "ஆழாக்கு": 5,
    "உழக்கு": 10,
    "நாழி": 50,
    "மரக்கால்": 100,
    "கலம்": 400
}

# ==========================================================
# 4. WATER / VALUE SYSTEM
# ==========================================================

VALUE_SCALE = {
    1: 1,
    5: 5,
    10: 10,
    50: 50,
    100: 100,
    500: 500,
    1000: 1000,
    10000: 10000,
    50000: 50000,
    100000: 100000,
    500000: 500000,
    1000000: 1000000
}

# ==========================================================
# 5. DONATION CLASSIFICATION ENGINE
# ==========================================================

def classify_donation(donation_type):
    """
    தான வகை அடையாளம்

    பாடல் 82:
    எண்ணளவு தானம் இருபத்து நான்கவற்றுள்^1
    மண்ணளவு தானம் வருமாகில் — ஒண்ணுதலாய்
    ஓராறு மைந்து ஒருநான்கு மோரிரண்டு
    சீரான ஏழுமெனச் செப்பு.

    Parameters
    ----------
    donation_type : str
        தான வகை

    Returns
    -------
    dict
        தான அளவீட்டு விவரம்
    """

    if donation_type not in DONATION_GROUPS:
        raise ValueError("தெரியாத தான வகை")

    return {
        "type": donation_type,
        "scale": DONATION_GROUPS[donation_type]
    }


# ==========================================================
# 6. FRACTION MAPPING ENGINE
# ==========================================================

def map_land_fraction(index):
    """
    நில அளவு fractional mapping

    பாடல் 82:
    1/320 → 1/160 → 1/80 → 1/20 → 1/4

    Parameters
    ----------
    index : int
        index position

    Returns
    -------
    float
        fractional value
    """

    if index < 0 or index >= len(LAND_FRACTIONS):
        raise ValueError("Index out of range")

    return LAND_FRACTIONS[index]


# ==========================================================
# 7. GRAIN CONVERSION SYSTEM
# ==========================================================

def convert_grain(unit, value):
    """
    தானிய அளவீட்டு மாற்றம்

    Parameters
    ----------
    unit : str
        தானிய வகை

    value : int | float
        அளவு

    Returns
    -------
    float
        கணக்கிடப்பட்ட மதிப்பு
    """

    if unit not in GRAIN_UNITS:
        raise ValueError("Unknown unit")

    return GRAIN_UNITS[unit] * value


# ==========================================================
# 8. VALUE SYSTEM
# ==========================================================

def value_scale_lookup(value):
    """
    மதிப்பு அளவீடு

    Parameters
    ----------
    value : int
        அளவு

    Returns
    -------
    int
        அளவிடப்பட்ட மதிப்பு
    """

    return VALUE_SCALE.get(value, None)


# ==========================================================
# 9. MAIN SUMMARY
# ==========================================================

def donation_summary():
    """
    முழு தான அமைப்பு சுருக்கம்

    Returns
    -------
    dict
        முழு mapping system
    """

    return {
        "groups": DONATION_GROUPS,
        "fractions": LAND_FRACTIONS,
        "grain_units": list(GRAIN_UNITS.keys()),
        "value_levels": list(VALUE_SCALE.keys())
    }


# ==========================================================
# 10. TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("===== DONATION SYSTEM =====")

    print(classify_donation("நிலவாய்"))
    print(map_land_fraction(2))
    print(convert_grain("நாழி", 2))
    print(value_scale_lookup(1000))
    print(donation_summary())