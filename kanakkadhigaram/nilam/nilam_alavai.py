"""
நில அளவை அறிதல் (Land Measurement System)
=========================================

Ancient Tamil land measurement system based on Kanakkadhigaram (பாடல்கள் 59–61).

Units:
- குழி
- மா
- வேலி
"""

# ==========================================================
# HIERARCHY
# ==========================================================

LAND_HIERARCHY = {
    "குழி": {"next": "மா", "factor": 100},
    "மா": {"next": "வேலி", "factor": 20}
}

# ==========================================================
# BASE BUILDER
# ==========================================================

def build_land_base():
    values = {"குழி": 1}

    order = ["குழி", "மா", "வேலி"]

    for i in range(len(order) - 1):
        parent = order[i]
        child = LAND_HIERARCHY[parent]["next"]
        factor = LAND_HIERARCHY[parent]["factor"]

        values[child] = values[parent] * factor

    return values


LAND_BASE = build_land_base()

# ==========================================================
# CORE FUNCTION
# ==========================================================

def convert_land(value, from_unit, to_unit):
    """
    பாடல் 59
    மாணாக்கிக் கொண்டதுகை நாலாறு சுழியாமல்
    வேலியதுவாம் மொழிவனென் — — —
    செவ்வாய்ப் பசுங்கிளியே சேமத்தி லொன்னறை
    ஒவ்வா திருப்பளவு மட்டுண்டு முன்னே.

    பாடல் 60
    மாறிய சாணாக்கு யேவரும் பன்னிரெண்டு டடிகோ லென்று
    வீறிலா மாவை நான்கு வேலிகொண்டுறு .........
    மீறிவா வெண்ணில் இரண்டால் இருநூத் தன்பத் தாறுங்
    கூறிய குழியாம் பாண்டி பாகங் குறித்துக் கூறே.

    பாடல் 61
    கூறிய தொண்டை யாகி குழியொரு வட்டில் சேர
    நாடறு நாழிக் காலால் இலையாத்துக் கண்ட மாகும்
    கோடறி விண்டே யொன்பது னாயிரக் கல்வித் தெறிய
    நாடொறும் எண்ணி லாத நல்லதோர் விகற்பம் தாளே.

    Parameters:
        value (float|int): அளவு
        from_unit (str): ஆரம்ப அலகு
        to_unit (str): இலக்கு அலகு

    Returns:
        float: மாற்றிய மதிப்பு
    """
    
    if from_unit not in LAND_BASE:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in LAND_BASE:
        raise ValueError(f"Unknown unit: {to_unit}")

    base = value * LAND_BASE[from_unit]
    return base / LAND_BASE[to_unit]

# ==========================================================
# UTILITIES
# ==========================================================

def list_land_units():
    return list(LAND_BASE.keys())

# ==========================================================
# TEST BLOCK 
# ==========================================================

if __name__ == "__main__":

    print("Available Units:", list_land_units())

    print("\nSample Conversions:")

    print("1 மா → குழி:", convert_land(1, "மா", "குழி"))
    print("1 வேலி → மா:", convert_land(1, "வேலி", "மா"))