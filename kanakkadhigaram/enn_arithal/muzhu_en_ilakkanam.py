"""
முழு எண்களின் இலக்கணம் (Large Number System)

கணக்கதிகாரம் நூலில் உள்ள பாடல்கள் 16 முதல் 19 வரை
மிகப்பெரிய எண்களின் படிநிலை அமைப்புகளை விளக்குகிறது.

------------------------------------------------------------

Large Number Hierarchy System

This module implements an exponential large-number scale system
based on ancient Tamil mathematical verses from "Kanakkadhigaram".

Each step increases by a factor of 10,000,000 (10⁷ scale progression).
"""

# =========================================================
# LARGE NUMBER HIERARCHY (10⁷ SCALE SYSTEM)
# =========================================================

LARGE_NUMBER_HIERARCHY = {
    "அனந்தம்": {"next": "மகாஉற்பலம்", "factor": 10_000_000},
    "மகாஉற்பலம்": {"next": "உற்பலம்", "factor": 10_000_000},
    "உற்பலம்": {"next": "மகாஅற்புதம்", "factor": 10_000_000},
    "மகாஅற்புதம்": {"next": "அற்புதம்", "factor": 10_000_000},
    "அற்புதம்": {"next": "மகாகனவளை", "factor": 10_000_000},
    "மகாகனவளை": {"next": "கனவளை", "factor": 10_000_000},
    "கனவளை": {"next": "மகாதன்பனை", "factor": 10_000_000},
    "மகாதன்பனை": {"next": "தன்பனை", "factor": 10_000_000},
    "தன்பனை": {"next": "மகாவலம்புரி", "factor": 10_000_000},
    "மகாவலம்புரி": {"next": "வலம்புரி", "factor": 10_000_000},
    "வலம்புரி": {"next": "மகாசஞ்சலம்", "factor": 10_000_000},
    "மகாசஞ்சலம்": {"next": "சஞ்சலம்", "factor": 10_000_000},
    "சஞ்சலம்": {"next": "மகாபிரளயம்", "factor": 10_000_000},
    "மகாபிரளயம்": {"next": "பிரளயம்", "factor": 10_000_000},
    "பிரளயம்": {"next": "மகாவெள்ளம்", "factor": 10_000_000},
    "மகாவெள்ளம்": {"next": "வெள்ளம்", "factor": 10_000_000},
    "வெள்ளம்": {"next": "மகாசமுத்திரம்", "factor": 10_000_000},
    "மகாசமுத்திரம்": {"next": "சமுத்திரம்", "factor": 10_000_000},
    "சமுத்திரம்": {"next": "மாகுமிர்தம்", "factor": 10_000_000},
    "மாகுமிர்தம்": {"next": "குமிர்தம்", "factor": 10_000_000},
    "குமிர்தம்": {"next": "மகாபதுமம்", "factor": 10_000_000},
    "மகாபதுமம்": {"next": "பதுமம்", "factor": 10_000_000},
    "பதுமம்": {"next": "மகாவிந்தம்", "factor": 10_000_000},
    "மகாவிந்தம்": {"next": "விந்தம்", "factor": 10_000_000},
    "விந்தம்": {"next": "மகாசங்கம்", "factor": 10_000_000},
    "மகாசங்கம்": {"next": "சங்கம்", "factor": 10_000_000},
    "சங்கம்": {"next": "மாகோடி", "factor": 10_000_000}
}

def find_root(h):
    parents = set(h.keys())
    children = {v["next"] for v in h.values()}
    return list(children - parents)[0]

def build_large_number_base_values():
    root = find_root(LARGE_NUMBER_HIERARCHY)

    values = {
        root: 1,
        "கோடி": 1   
    }

    queue = [root]

    while queue:
        current = queue.pop(0)

        for parent, details in LARGE_NUMBER_HIERARCHY.items():
            if details["next"] == current and parent not in values:
                values[parent] = values[current] * details["factor"]
                queue.append(parent)

    return values
LARGE_NUMBER_BASE_VALUES = build_large_number_base_values()

# =========================================================
# CONVERSION FUNCTION
# =========================================================

def convert_large_number(value, from_unit, to_unit):
    """
    பாடல் 16
    கோடி யுடன்சங்கம் விந்தம்சூழ் பதுமம்
    நாடு சமுத்திரத்தின் மேல்வெள்ளம் - நீடு
    பிரளயமா மென்றவற்றின் பேர்தோறும் பெற்ற
    புரளயமா மென்றே புகல்.

    பாடல் 17
    மாகமுந் தன்பனையு மற்புதமு முற்பலமும்
    ஏக அனந்தமுடன் வேணுவுமாந் - தோகாய்
    சலஞ்சலமு மந்தாரையுந் தாரகையு மேரு
    வலம்புரியின் பின்புதல்வோர் மாட்டு

    பாடல் 18
    நற்கோடி நற்சங்கு நல்விந்தம் நல்பதுமம்
    மற்கோ சமுத்திரம் வெள்ளம் பிரளயம்
    சஞ்சலம் வலம்புரி கள்ள விழங்கு
    அமுர்தங் காண அகற்பணி கற்பம்
    கூட்டிய தன்பனை யுற்பதாய் அனந்தம்
    கறவைக் கறிவோர் அறிந்தவை யானவர்
    இன்னம் பெறுவர் அறிந்து.

    பாடல் 19
    கோடியும் சங்கமும் விந்தம் பதுமம் கூங்கடலும்
    நாடிய வெள்ளம் பிரளயம் தன்பனை நாயகத்தனை
    தேடிய யோர்தரும் மாதவ ராதித் திருவருளால்
    நீடிய லக்க முரைத்தது மாமிது நேரிழையே.

    Parameters
    ----------
    value : int | float
        மாற்ற வேண்டிய அளவு

    from_unit : str
        ஆரம்ப அலகு

    to_unit : str
        இலக்கு அலகு

    Returns
    -------
    float
        மாற்றிய மதிப்பு
    """

    if from_unit not in LARGE_NUMBER_BASE_VALUES:
        raise ValueError(f"தெரியாத அலகு: {from_unit}")

    if to_unit not in LARGE_NUMBER_BASE_VALUES:
        raise ValueError(f"தெரியாத அலகு: {to_unit}")

    value_in_base = value * LARGE_NUMBER_BASE_VALUES[from_unit]
    return value_in_base / LARGE_NUMBER_BASE_VALUES[to_unit]


# =========================================================
# UTILITIES
# =========================================================

def list_large_number_units():
    """Return all supported large number units."""
    return list(LARGE_NUMBER_BASE_VALUES.keys())


# =========================================================
# TEST CASES
# =========================================================

if __name__ == "__main__":
    print("\n===== LARGE NUMBER SYSTEM TESTS =====")

    # List all units
    print("\n--- Supported Units ---")
    print(list_large_number_units())

    # Basic forward conversion
    print("\n--- Basic Conversions ---")
    print("1 கோடி =", convert_large_number(1, "கோடி", "சங்கம்"), "சங்கம்")
    print("1 சங்கம் =", convert_large_number(1, "சங்கம்", "விந்தம்"), "விந்தம்")
    print("1 விந்தம் =", convert_large_number(1, "விந்தம்", "பதுமம்"), "பதுமம்")

    # Reverse conversion
    print("\n--- Reverse Conversions ---")
    print("1 மகாசமுத்திரம் =", convert_large_number(1, "மகாசமுத்திரம்", "வெள்ளம்"), "வெள்ளம்")
    print("1 பிரளயம் =", convert_large_number(1, "பிரளயம்", "மகாபிரளயம்"), "மகாபிரளயம்")

    # Cross-level deep conversion
    print("\n--- Deep Conversion ---")
    print("1 அனந்தம் =", convert_large_number(1, "அனந்தம்", "மாகோடி"), "மாகோடி")

    # Large jump test
    print("\n--- Large Jump Test ---")
    print("1 கோடி =", convert_large_number(1, "கோடி", "மாகோடி"), "மாகோடி")

    # Edge / symmetry test (back and forth)
    print("\n--- Symmetry Test ---")
    v = convert_large_number(1, "அற்புதம்", "சங்கம்")
    print("1 அற்புதம் =", v, "சங்கம்")
    print("Back:", convert_large_number(v, "சங்கம்", "அற்புதம்"), "அற்புதம்")

    # Error handling test
    print("\n--- Error Test ---")
    try:
        convert_large_number(1, "கோடி", "INVALID")
    except ValueError as e:
        print("Caught error:", e)