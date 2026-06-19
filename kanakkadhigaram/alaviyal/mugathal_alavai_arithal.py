"""
முகத்தல் அளவை அறிதல் (Mugathal Alavai System)
===========================================

Ancient Tamil volume/capacity measurement system
based on Kanakkadhigaram (பாடல்கள் 54-56).

This module includes:
- Hierarchical volume conversion system
- Base unit normalization using 'மனம்'
"""

# ==========================================================
# 1. HIERARCHY
# ==========================================================

MUGATHAL_HIERARCHY = {
    "மனம்": {"next": "புகை", "factor": 100},
    "புகை": {"next": "பால்", "factor": 100},
    "பால்": {"next": "தண்ணீர்", "factor": 100},
    "தண்ணீர்": {"next": "நெய்", "factor": 100},
    "நெய்": {"next": "செலம்", "factor": 100},
    "செலம்": {"next": "விந்து", "factor": 100},
    "விந்து": {"next": "துளி", "factor": 100},
    "துளி": {"next": "துருவம்", "factor": 100},
    "துருவம்": {"next": "செவிடு", "factor": 100},

    "செவிடு": {"next": "ஆழாக்கு", "factor": 5},
    "ஆழாக்கு": {"next": "உழக்கு", "factor": 2},
    "உழக்கு": {"next": "நாழி", "factor": 4},
    "நாழி": {"next": "குறுணி", "factor": 8},
    "குறுணி": {"next": "தூணி", "factor": 4},
    "தூணி": {"next": "கலம்", "factor": 3}
}

# ==========================================================
# 2. BASE VALUE BUILDER
# ==========================================================

def build_mugathal_base_values():
    values = {"மனம்": 1}
    current = "மனம்"

    while current in MUGATHAL_HIERARCHY:
        nxt = MUGATHAL_HIERARCHY[current]["next"]
        factor = MUGATHAL_HIERARCHY[current]["factor"]

        values[nxt] = values[current] * factor
        current = nxt

    return values


MUGATHAL_BASE_VALUES = build_mugathal_base_values()

# ==========================================================
# 3. CONVERSION ENGINE
# ==========================================================

def convert_mugathal(value, from_unit, to_unit):

    """
    பாடல் 54
    ஆறிய மனமே தூவம் அதுபுகை பால்அப்பு நெய்யே
    சீறிய சலமே விந்து சிறுதுளி துருவஞ் செவிடு
    மீறிய நூறே சாலி யிருபத் தோன மன்பன்
    நிற்றியொன்றே கால யேளளவு யெட்டி லொன்றே.

    பாடல் 55
    ஆய்ந்த செவிடைந்தே ஆழாக்கு ரண்டுழக்காம்
    வாய்ந்ததொரு நாலாகில் நாழியாம் — ஏந்திழையாய்
    எட்டாய்க் குறுணியாம் ஈரண்டாய் தூணியாங்
    கட்டான மூன்றே கலம்.

    பாடல் 56

    உழக்குரெண் டுரியே யாகும் உயிரிரண் டொன்றே நாழி
    அளக்குமின் நாழி எட்டே ஆங்கொரு குறுணி யாகும்
    முழக்கமாங் குறுணி நாலே மொழிந்திடில் தூணி யாகும்
    பழுப்பிலாத் தூணி மூன்றே பகர்ந்தனர் கலமென் றே.

    Parameters
    ----------
    value : float
        மாற்ற வேண்டிய அளவு.

    from_unit : str
        ஆரம்ப அலகு.

    to_unit : str
        இலக்கு அலகு.

    Returns
    -------
    float
        மாற்றிய அளவு.
    """

    if from_unit not in MUGATHAL_BASE_VALUES:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in MUGATHAL_BASE_VALUES:
        raise ValueError(f"Unknown unit: {to_unit}")

    base = value * MUGATHAL_BASE_VALUES[from_unit]
    return base / MUGATHAL_BASE_VALUES[to_unit]

# ==========================================================
# 4. UTILITIES
# ==========================================================

def list_mugathal_units():
    return list(MUGATHAL_BASE_VALUES.keys())

def get_mugathal_value(unit):
    return MUGATHAL_BASE_VALUES.get(unit)

# ==========================================================
# GRAIN - NAZHI SYSTEM (VERSE 63–65)
# ==========================================================

GRAIN_NAZHI = {
    "எள்ளு": 115200,
    "நெல்": 14400,
    "அரிசி": 18000,
    "பயறு": 14800,
    "அவரை": 1800,
    "மிளகு": 2860
}

def grain_to_count(grain, nazhi_count=1):
    """
    பாடல் 63
    நூறா யிரத்தொரு பத்தய்யா யிரத்திரு
    நூறுஎள்ளு மொருநாழி நெல்லிதனைச் — கூறுங்கால்
    எட்டெட்டு நெல்லிலக்க மாக்கிறே ழுவரிசிபத்
    தெட்டெண் ணாயிரமாம் பார்.

    பாடல் 64
    நாழி பயறுபதி னாலா யிரத்தெண்ணூ (று)
    ஆழித் திருநாள் அவரைத்தான் — கூறிவிடில்
    ஓரா யிரத்தொண்ணூ றென்றார் மிளகுபன
    நீரா யிரத்தொண்ணூ றெண்.

    பாடல் 65
    ஏத்திய பதினாயிரத்து நானூறு நெல்லு நாழி
    மாத்திய அரிசி பதினெண் ணாயிர மாகும்......
    பாத்திடு மெள்ளு லெங்குமொரு பதினைய்யா யிரத்திரு நூறு
    சாத்தரிய கணக்குத் தன்னை சரிவரப் பார்த்துக் கொண்டேன்.

    Parameters:
        grain (str): தானியம் பெயர்
        nazhi_count (int): நாழி எண்ணிக்கை

    Returns:
        int: மொத்த அளவு
    """
    if grain not in GRAIN_NAZHI:
        raise ValueError(f"Unknown grain: {grain}")
    return GRAIN_NAZHI[grain] * nazhi_count

def count_to_nazhi(count, grain):
    """grain count - Nazhi"""
    if grain not in GRAIN_NAZHI:
        raise ValueError(f"Unknown grain: {grain}")
    return count / GRAIN_NAZHI[grain]

def list_grains():
    return list(GRAIN_NAZHI.keys())

# ==========================================================
# TEST BLOCK 
# ==========================================================

if __name__ == "__main__":

    print("Available Units:")
    print(list_mugathal_units())

    print("\nSample Conversions:")

    print("1 கலம் → தூணி:", convert_mugathal(1, "கலம்", "தூணி"))
    print("1 தூணி → குறுணி:", convert_mugathal(1, "தூணி", "குறுணி"))
    print("1 செவிடு → மனம்:", convert_mugathal(1, "செவிடு", "மனம்"))
    print("3840 செவிடு → கலம்:", convert_mugathal(3840, "செவிடு", "கலம்"))

    print("\nGrain System Tests:")
    print("1 நாழி நெல் =", grain_to_count("நெல்", 1))
    print("14400 எள்ளு =", count_to_nazhi(14400, "எள்ளு"), "நாழி")