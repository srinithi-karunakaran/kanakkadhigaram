"""
நிறையளவும் முகத்தல் அளவும் (Verse 66–68 System)
=============================================

Clean normalized conversion system from Kanakkadhigaram:

Includes:
- Weight & Liquid (Verse 66)
- Material Nazhi (Verse 67)
- Bulk transport system (Verse 68)

All conversions normalized as:
    1 UNIT = BASE VALUE
"""

# ==========================================================
# ===================== VERSE 66 ============================
# ==========================================================

WEIGHT_LIQUID_66 = {

    # Core weight
    "கழஞ்சு": 1,
    "ஆழாக்கு": 5,

    # Water-based nazhi (ALL same unit: 1 நாழி = X பலம்)
    "நாழி_உத்தமம்": 12,
    "நாழி_மத்திமம்": 13,
    "நாழி_அதமம்": 17,

    # Trade bulk units
    "சுமை_துவர்ப்பாக்கு": 30,
    "பாரம்_மிளகு": 48,
    "பாரம்_புளி": 140,
    "சிரிமை_துவர்ப்பாக்கு": 10,

    # special mapping base
    "கற்பூரம்_ஆழாக்கு": 5
}

# ==========================================================
# ===================== VERSE 67 ============================
# ==========================================================

MATERIAL_NAZHI_67 = {

    # 1 நாழி = X பலம்
    "மண்": 17,
    "மணல்": 20,
    "நெல்": 11.25,
    "அரிசி": 12.5,
    "உப்பு": 16
}

# ==========================================================
# ===================== VERSE 68 ============================
# ==========================================================

BULK_68 = {

    # transport/packing system
    "நெற்பாரம்": 2,      # 2 தூணி
    "வைக்கோல்_கட்டு": 1,
    "புற்கட்டு": 1,
    "நாராசம்": 1,
    "மிளகு_பாரம்": 64
}

# ==========================================================
# ===================== CONVERTERS ==========================
# ==========================================================

def convert_weight(value, from_unit, to_unit):
    """
    பாடல் 66
    அஞ்சே கழஞ்சிடை ஆழாக்கு கற்பூரம்
    கொஞ்சார் கிளிமொழியார் கோகிலமே — மிஞ்சாது
    நன்றான தண்ணிக்கு நாழிபலம் மென்றாகி
    ஒன்றிரண்டா மென்றே உரை.

    Parameters:
        value (float|int): அளவு
        from_unit (str): ஆரம்ப அலகு
        to_unit (str): இலக்கு அலகு

    Returns:
        float: மாற்றிய மதிப்பு
    """
    if from_unit not in WEIGHT_LIQUID_66 or to_unit not in WEIGHT_LIQUID_66:
        raise ValueError("Unknown unit")

    base = value * WEIGHT_LIQUID_66[from_unit]
    return base / WEIGHT_LIQUID_66[to_unit]


def convert_nazhi_material(value, material):
    """
    பாடல் 67
    மண்ணு மணலுமொழி நாழி^1 வைத்தயிடை
    எண்ணிற் பதினே ழிருபதாம் - தெண்ணரிய (நெல்லரிசி)
    ஐங்காலும் ஐயரையும் அத்துடனே பத்தாறு^2
    பஞ்சாறு முன்பின் பலம்.

    Parameters:
        material (str): பொருள் பெயர்
        nazhi_count (int): நாழி எண்ணிக்கை

    Returns:
        float: மொத்த பலம்
    """
    if material not in MATERIAL_NAZHI_67:
        raise ValueError("Unknown material")

    return value * MATERIAL_NAZHI_67[material]


def convert_bulk(value, from_unit, to_unit):
    """
    பாடல் 68
    வைக்கோல் திரைகல் இருதூணி நெற்பாரம்
    உப்புரைக்கின் கல்தூணி உள்ளநிறை — புற்கட்டு
    எட்டெட்டு நாராசம் என்பர்மிள கின்பாரம்
    மட்டிட்டுச் சொல்வார் மதித்து.

    Parameters:
        value (float|int): அளவு
        from_unit (str): ஆரம்ப அலகு
        to_unit (str): இலக்கு அலகு

    Returns:
        float: மாற்றிய மதிப்பு
    """
    if from_unit not in BULK_68 or to_unit not in BULK_68:
        raise ValueError("Unknown bulk unit")

    base = value * BULK_68[from_unit]
    return base / BULK_68[to_unit]

# ==========================================================
# ===================== UTILITIES ===========================
# ==========================================================

def list_weight_units():
    return list(WEIGHT_LIQUID_66.keys())

def list_materials():
    return list(MATERIAL_NAZHI_67.keys())

def list_bulk_units():
    return list(BULK_68.keys())

# ==========================================================
# ===================== TEST CASES ==========================
# ==========================================================

if __name__ == "__main__":

    print("===== VERSE 66 =====")
    print(convert_weight(5, "கழஞ்சு", "ஆழாக்கு"))
    print(convert_weight(1, "பாரம்_மிளகு", "சுமை_துவர்ப்பாக்கு"))

    print("\n===== VERSE 67 =====")
    print(convert_nazhi_material(1, "நெல்"))
    print(convert_nazhi_material(2, "அரிசி"))

    print("\n===== VERSE 68 =====")
    print(convert_bulk(2, "நெற்பாரம்", "வைக்கோல்_கட்டு"))
    print(convert_bulk(1, "மிளகு_பாரம்", "நாராசம்"))

    print("\nLISTS:")
    print(list_weight_units())
    print(list_materials())
    print(list_bulk_units())