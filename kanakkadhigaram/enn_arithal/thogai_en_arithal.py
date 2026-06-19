"""
தொகை எண் அறிதல் (Thogai En Arithal System)

கணக்கதிகாரம் நூலில் உள்ள தொகை, படை, மற்றும் சிறப்பு எண்ணிக்கை அமைப்புகள்
அடிப்படையாகக் கொண்ட கணித மாற்று முறைமை.

------------------------------------------------------------

Thogai Number Arithmetic System

This module implements ancient Tamil counting systems
based on "Kanakkadhigadhigaram", including:

- Army hierarchy system (படை அமைப்பு)
- Large-scale count units (எண்ணிக்கை அளவுகள்)
- Special commodity count systems
"""


# =========================================================
# 1. ARMY HIERARCHY SYSTEM
# =========================================================

ARMY_HIERARCHY = {
    "அக்குரோணி": {"next": "தண்டு", "factor": 100},
    "தண்டு": {"next": "பதாதி", "factor": 82}
}

PADATHI_COMPOSITION = {
    "ஆனை": 3,
    "தேர்": 10,
    "குதிரை": 100,
    "காலாள்": 1000
}


def build_army_base_values():
    values = {"பதாதி": 1}
    items = list(ARMY_HIERARCHY.items())

    for parent, details in reversed(items):
        child = details["next"]
        values[parent] = values[child] * details["factor"]

    return values


ARMY_BASE_VALUES = build_army_base_values()


def convert_army(value, from_unit, to_unit):
    """
    பாடல் 20 (Army Conversion System)

    கரிபத்து தேர்மூன்று காலாளோராயிரம்
    பரிநூ றாகும் பதாதி - வருமவை கேள்
    எண்பத் திருமடங்கு தண்டா மிவைநூறும்
    கொண்டது அக்குரோணி கூறு.

    Description:
    1 பதாதி =
        3 ஆனை
        10 தேர்
        100 குதிரை
        1000 காலாள்

    82 பதாதி = 1 தண்டு
    100 தண்டு = 1 அக்குரோணி

    Parameters
    ----------
    value : float | int
        Value to convert

    from_unit : str
        Source unit (Tamil name)

    to_unit : str
        Target unit (Tamil name)

    Returns
    -------
    float
        Converted value
    """

    valid_units = set(ARMY_BASE_VALUES) | set(PADATHI_COMPOSITION)

    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError("தெரியாத அலகு (Unknown unit)")

    if from_unit in ARMY_BASE_VALUES and to_unit in ARMY_BASE_VALUES:
        base = value * ARMY_BASE_VALUES[from_unit]
        return base / ARMY_BASE_VALUES[to_unit]

    if from_unit in PADATHI_COMPOSITION and to_unit in PADATHI_COMPOSITION:
        base = value * PADATHI_COMPOSITION[from_unit]
        return base / PADATHI_COMPOSITION[to_unit]

    if from_unit in ARMY_BASE_VALUES and to_unit in PADATHI_COMPOSITION:
        base = value * ARMY_BASE_VALUES[from_unit]
        return base * PADATHI_COMPOSITION[to_unit]

    if from_unit in PADATHI_COMPOSITION and to_unit in ARMY_BASE_VALUES:
        base = value / PADATHI_COMPOSITION[from_unit]
        return base / ARMY_BASE_VALUES[to_unit]

    raise ValueError("இந்த அலகுகளுக்கு நேரடி மாற்றம் இல்லை")


def list_army_units():
    return list(ARMY_BASE_VALUES) + list(PADATHI_COMPOSITION)


# =========================================================
# 2. COUNT SYSTEM
# =========================================================

COUNT_UNITS = {
    "லட்சம்": {"base": "காலாள்", "factor": 100000},
    "அலகு": {"base": "பாக்கு", "factor": 100000},
    "கோடி": {"base": "பட்டுப்பட்டாரம்", "factor": 21}
}

def convert_count(value, from_unit, to_unit):
    """
    பாடல் 21 (Count System)

    ஒரு படைக் காலாள் ஒரு லட்சம் லட்சம்
    கருதைக் காயோ ரலகாகுந் திரிகிலாப்
    பாருலகிற் பட்டிப் படிமுறுக்குள் மூவேழு
    சேருமது கோடியெனச் செப்பு.

    Parameters
    ----------
    value : float | int
        Input value

    from_unit : str
        Source unit

    to_unit : str
        Target unit

    Returns
    -------
    float
        Converted value
    """

    def normalize(unit, value):
        for k, v in COUNT_UNITS.items():
            if unit == k:
                return value * v["factor"], v["base"]
            if unit == v["base"]:
                return value, v["base"]
        return None, None

    val1, base1 = normalize(from_unit, value)
    val2, base2 = normalize(to_unit, 1)

    if base1 is None or base2 is None:
        raise ValueError("தெரியாத அலகு")

    if base1 != base2:
        raise ValueError("இந்த அலகுகள் இணைக்க முடியாது")

    return val1 / val2


def list_count_units():
    return ["லட்சம்", "காலாள்", "அலகு", "பாக்கு", "கோடி", "பட்டுப்பட்டாரம்"]


# =========================================================
# 3. SPECIAL COUNT SYSTEM
# =========================================================

SPECIAL_COUNTS = {
    "அணி": {"base": "ஆனை", "factor": 5},
    "மொத்தம்": {"base": "குதிரை", "factor": 80},
    "திறம்": {"base": "ஆடு", "factor": 80},
    "பொதி": {"base": "அச்சுவெல்லம்", "factor": 6000},
    "அவணம்": {"base": "கொட்டைப்பாக்கு", "factor": 10000},
    "அம்மணம்": {"base": "கொட்டைப்பாக்கு", "factor": 20000},
    "சட்டை": {"base": "தேங்காய்", "factor": 310}
}


def convert_special_count(value, from_unit, to_unit):
    """
    பாடல் 22 (Special Count System)

    அத்தி யோரைந்து அணியாகும் அடல்பரி
    மொத்த மெண்ப தொருமொத்தம் - அத்தகையென்
    ஆடமே யாமென்று வருகோ ரெண்பதாங்
    கடிவத் திறமென்று கூறு.

    Parameters
    ----------
    value : float | int
        Input value

    from_unit : str
        Source unit

    to_unit : str
        Target unit

    Returns
    -------
    float
        Converted value
    """

    def convert(unit, value):
        for big, data in SPECIAL_COUNTS.items():
            if unit == big:
                return value * data["factor"]
            if unit == data["base"]:
                return value
        raise ValueError("தெரியாத அலகு")

    for big, data in SPECIAL_COUNTS.items():
        if from_unit in [big, data["base"]] and to_unit in [big, data["base"]]:
            base = convert(from_unit, value)

            if to_unit == big:
                return base / data["factor"]
            return base

    raise ValueError("இந்த அலகுகளுக்கு மாற்றம் இல்லை")


def list_special_count_units():

    units = set()
    for k, v in SPECIAL_COUNTS.items():
        units.add(k)
        units.add(v["base"])
    return list(units)

if __name__ == "__main__":
    print("\n===== THOGAI EN ARITHAL SYSTEM TESTS =====")

    # =====================================================
    # 1. ARMY SYSTEM TESTS
    # =====================================================
    print("\n--- ARMY SYSTEM ---")

    print("Supported Units:")
    print(list_army_units())

    print("\nBasic Conversions:")
    print("1 தண்டு → பதாதி =", convert_army(1, "தண்டு", "பதாதி"))
    print("1 அக்குரோணி → தண்டு =", convert_army(1, "அக்குரோணி", "தண்டு"))

    print("\nPadathi Composition:")
    print("1 பதாதி → ஆனை =", convert_army(1, "பதாதி", "ஆனை"))
    print("10 தேர் → காலாள் =", convert_army(10, "தேர்", "காலாள்"))

    print("\nCross Conversion:")
    print("1 அக்குரோணி → ஆனை =", convert_army(1, "அக்குரோணி", "ஆனை"))

    # =====================================================
    # 2. COUNT SYSTEM TESTS
    # =====================================================
    print("\n--- COUNT SYSTEM ---")

    print("Supported Units:")
    print(list_count_units())

    print("\nBasic Conversion:")
    print("1 லட்சம் → காலாள் =", convert_count(1, "லட்சம்", "காலாள்"))
    print("1 கோடி → பட்டுப்பட்டாரம் =", convert_count(1, "கோடி", "பட்டுப்பட்டாரம்"))

    print("\nReverse Conversion:")
    print("1 காலாள் → லட்சம் =", convert_count(1, "காலாள்", "லட்சம்"))

    # =====================================================
    # 3. SPECIAL COUNT SYSTEM TESTS
    # =====================================================
    print("\n--- SPECIAL COUNT SYSTEM ---")

    print("Supported Units:")
    print(list_special_count_units())

    print("\nBasic Conversion:")
    print("1 அணி → ஆனை =", convert_special_count(1, "அணி", "ஆனை"))
    print("5 ஆனை → அணி =", convert_special_count(5, "ஆனை", "அணி"))

    print("\nAnother Conversion:")
    print("1 மொத்தம் → குதிரை =", convert_special_count(1, "மொத்தம்", "குதிரை"))

    # =====================================================
    # ERROR TESTS
    # =====================================================
    print("\n--- ERROR TESTS ---")

    try:
        convert_army(1, "தண்டு", "INVALID")
    except Exception as e:
        print("Army Error:", e)

    try:
        convert_count(1, "லட்சம்", "INVALID")
    except Exception as e:
        print("Count Error:", e)

    try:
        convert_special_count(1, "அணி", "INVALID")
    except Exception as e:
        print("Special Error:", e)