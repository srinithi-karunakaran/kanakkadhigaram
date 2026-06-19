"""
கால அளவு அறிதல் : பாடல் 40 (Kaala 40 Cosmology System)
======================================================

இந்த தொகுதி கணக்கதிகாரம் நூலில் உள்ள பிரபஞ்ச கால அளவீட்டு
முறையை அடிப்படையாகக் கொண்டு உருவாக்கப்பட்டுள்ளது.

------------------------------------------------------
This module implements a symbolic cosmological time hierarchy of "Kanakkadhigaram".

It provides:
- Hierarchical time unit system

"""

# ==========================================================
# HIERARCHY (VERSE 40)
# ==========================================================

KAALA_40_HIERARCHY = {
    "சதுர்யுகம்": {"next": "மகாயுகம்", "factor": 2000},
    "மகாயுகம்": {"next": "மனு ஆட்சி", "factor": 18},
    "மனு ஆட்சி": {"next": "இந்திர ஆட்சி", "factor": 70},
    "இந்திர ஆட்சி": {"next": "பிரம்மா இரவு", "factor": 27},
    "பிரம்மா இரவு": {"next": "பிரம்மா மாதம்", "factor": 30},
    "பிரம்மா மாதம்": {"next": "பிரம்மா ஆண்டு", "factor": 12},
    "பிரம்மா ஆண்டு": {"next": "பிரம்மா ஆயுள்", "factor": 100},
    "பிரம்மா ஆயுள்": {"next": "கற்ப காலம்", "factor": 360},
    "கற்ப காலம்": {"next": "மகா கற்பம்", "factor": 100},
    "மகா கற்பம்": {"next": "ரோம மகரிஷி மயிர்", "factor": 100},
    "ரோம மகரிஷி மயிர்": {"next": "மீன மகரிஷி செதில்", "factor": 100},
    "மீன மகரிஷி செதில்": {"next": "வித்துவாசன் நிமிடம்", "factor": 100},
    "வித்துவாசன் நிமிடம்": {"next": "மகாசக்தி நிமிடம்", "factor": 100},
    "மகாசக்தி நிமிடம்": {"next": "சர்வேசுவரன் நிமிடம்", "factor": 180}
}

# ==========================================================
# BASE VALUE BUILDER
# ==========================================================

def build_prabhanja_kaala_base_values():
    """
    சதுர்யுகம் அடிப்படையாக கொண்டு அனைத்து அலகுகளையும் கணக்கிடும்.
    """

    values = {"சதுர்யுகம்": 1}

    for parent, details in KAALA_40_HIERARCHY.items():
        child = details["next"]
        factor = details["factor"]

        if parent not in values:
            continue  # safety guard

        values[child] = values[parent] * factor

    return values


KAALA_40_BASE_VALUES = build_prabhanja_kaala_base_values()

# ==========================================================
# CORE CONVERTER
# ==========================================================

def convert_prabhanja_kaala(value, from_unit, to_unit):
    """
    பாடல் 40 - பிரபஞ்ச கால மாற்றி
    கண்ணுஞ் சதுர்யுக ரண்டாயிரம் கொண்டது
    நன்று பிர்மார்க்கு நாளொன்று — பெண்ணணங்கே
    ஐயாறு திங்கள் ஆறிரண்டே ஆண்டாகும்
    பொய்யாக நூறு புகும்.

    Parameters
    ----------
    value : float | int
        மாற்ற வேண்டிய மதிப்பு

    from_unit : str
        தொடக்க அலகு

    to_unit : str
        இலக்கு அலகு

    Returns
    -------
    float
        மாற்றப்பட்ட மதிப்பு
    """

    if from_unit not in KAALA_40_BASE_VALUES:
        raise ValueError(f"தெரியாத அலகு: {from_unit}")

    if to_unit not in KAALA_40_BASE_VALUES:
        raise ValueError(f"தெரியாத அலகு: {to_unit}")

    base = value * KAALA_40_BASE_VALUES[from_unit]
    return base / KAALA_40_BASE_VALUES[to_unit]


# ==========================================================
# UTILITIES 
# ==========================================================

def list_prabhanja_kaala_units():
    """அனைத்து கால அலகுகளையும் தரும்"""
    return list(KAALA_40_BASE_VALUES.keys())


def get_prabhanja_kaala_chain():
    """hierarchy structure return செய்கிறது"""
    return KAALA_40_HIERARCHY


# ==========================================================
# TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print(list_prabhanja_kaala_units())

    print("\n=== SAMPLE CONVERSIONS ===")
    print("1 சதுர்யுகம் → மகாயுகம் =", convert_prabhanja_kaala(1, "சதுர்யுகம்", "மகாயுகம்"))

    print("1 மகாயுகம் → மனு ஆட்சி =", convert_prabhanja_kaala(1, "மகாயுகம்", "மனு ஆட்சி"))

    print("1 கற்ப காலம் → மகா கற்பம் =", convert_prabhanja_kaala(1, "கற்ப காலம்", "மகா கற்பம்"))