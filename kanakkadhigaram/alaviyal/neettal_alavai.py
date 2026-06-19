"""
நீட்டல் அளவை அறிதல் (Neettal Alavai System)
==========================================

கணக்கதிகாரம் நூலில் உள்ள நீட்டல் அளவீட்டு முறைகளை அடிப்படையாகக் கொண்டு
மிகச் சிறிய அளவிலிருந்து மிகப் பெரிய தூர அளவுகள் வரை மாற்றும்
பாரம்பரிய தமிழ் கணித அமைப்பு இம்மொட்யூலில் செயல்படுத்தப்பட்டுள்ளது.

இதில் உள்ளவை:
- அணு முதல் யோசனை வரை நீட்டல் அளவீட்டு முறை
- இரட்டிப்பு மற்றும் பல்கூட்டல் அடிப்படையிலான hierarchy system
- பாரம்பரிய பாடல் அடிப்படையிலான unit conversion

------------------------------------------------------------

This module implements ancient Tamil length measurement systems
from Kanakkadhigaram.

It includes:
- Hierarchical length unit conversions (Atom → Yojanai)
- Multiplicative scaling rules (8, 12, 2, 4, 500 etc.)
- Verse-based traditional measurement mapping
- Conversion between viral and muzham

"""

# ==========================================================
# 1. LENGTH HIERARCHY SYSTEM (VERSE 41–45)
# ==========================================================

NEETTAL_HIERARCHY = {
    "அணு": {"next": "துகள்", "factor": 8},
    "துகள்": {"next": "பஞ்சிற்றுளி", "factor": 8},
    "பஞ்சிற்றுளி": {"next": "மயிர்நுனை", "factor": 8},
    "மயிர்நுனை": {"next": "நேர்மணல்", "factor": 8},

    "நேர்மணல்": {"next": "கடுகு", "factor": 8},
    "கடுகு": {"next": "எள்ளு", "factor": 8},
    "எள்ளு": {"next": "நெல்", "factor": 8},
    "நெல்": {"next": "விரல்", "factor": 8},

    "விரல்": {"next": "சாண்", "factor": 12},
    "சாண்": {"next": "முழம்", "factor": 2},
    "முழம்": {"next": "சிறுகோல்", "factor": 2},
    "சிறுகோல்": {"next": "பெருங்கோல்", "factor": 4},

    "பெருங்கோல்": {"next": "கூப்பிடு", "factor": 500},
    "கூப்பிடு": {"next": "காதம்", "factor": 4},
    "காதம்": {"next": "யோசனை", "factor": 4}
}

def build_neettal_base_values():
    values = {"அணு": 1}
    current = "அணு"

    while current in NEETTAL_HIERARCHY:
        nxt = NEETTAL_HIERARCHY[current]["next"]
        factor = NEETTAL_HIERARCHY[current]["factor"]

        values[nxt] = values[current] * factor
        current = nxt

    return values

NEETTAL_BASE_VALUES = build_neettal_base_values()

# ==========================================================
# 2. LENGTH CONVERSION ENGINE
# ==========================================================

def convert_length(value, from_unit, to_unit):
    """
    Convert between Tamil traditional length units.
    """

    if from_unit not in NEETTAL_BASE_VALUES:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in NEETTAL_BASE_VALUES:
        raise ValueError(f"Unknown unit: {to_unit}")

    base = value * NEETTAL_BASE_VALUES[from_unit]
    return base / NEETTAL_BASE_VALUES[to_unit]


def list_length_units():
    return list(NEETTAL_BASE_VALUES.keys())

# ==========================================================
# 3. VIRAL SYSTEM (VERSE 51)
# ==========================================================

VIRAL_NEL_MAP = {
    "உத்தம விரல்": 8,
    "மத்திம விரல்": 7,
    "அதம விரல்": 6
}

MUZHAM_FACTOR = 9


def list_viral_types():
    """
    பாடல் 51
    உத்தமம் எட்டே ஏழும் மத்திமம் ஆறும் ஆக
    ஒத்தநெல் அவற்றினாலே ஒருவிரல் அளவ தாகும்
    வைத்ததன் திசைகள் தோறும் வழங்கினான் முழக்கோல் என்று
    நெய்த்திருள் சுருண்ட கூந்தல் நெளிமயிர் சாய லாளே.
    """
    return list(VIRAL_NEL_MAP.keys())


def get_nel_count(viral_type):
    if viral_type not in VIRAL_NEL_MAP:
        raise ValueError(f"Unknown viral type: {viral_type}")
    return VIRAL_NEL_MAP[viral_type]


def get_viral_type(nel_count):
    for v, n in VIRAL_NEL_MAP.items():
        if n == nel_count:
            return v
    raise ValueError(f"No viral type for {nel_count} nel")


def viral_to_muzham(viral_count):
    return viral_count / MUZHAM_FACTOR


def muzham_to_viral(muzham_count):
    return muzham_count * MUZHAM_FACTOR


def get_all_viral_mappings():
    return VIRAL_NEL_MAP.copy()

# ==========================================================
# VERSE 98 
# ==========================================================

def saan_to_mulam(saan: float) -> float:
    """
    பாடல் 98 - நீட்டல் அளவு (சாண் → முழம்)

    எட்டளவிற் சாணோடே மார்பதி ளஞ்சுகபே
    வரைமா விற்றான் பெருக்கி—இட்டதொகை
    அ...கை காலிற் கழிக்கமுழம் நாலரையா
    மென்றுரைக்கத் தூணாத மாங்கு.

    Logic:
    ------
    1 Saan = 12 viral units
    scaled by 8
    correction /40
    final ÷ 4.5 → Mulam
    """

    viral_units = saan * 12
    scaled = viral_units * 8
    correction = scaled / 40
    net = scaled - correction

    return net / 4.5


def mulam_to_saan(mulam: float) -> float:
    """
    Reverse of Verse 98 logic
    """

    estimated = mulam * 4.5
    adjusted = estimated + (estimated / 40)
    return adjusted / 96


def explain_saan_conversion(saan: float):
    """
    Step-by-step breakdown (Verse 98 debug view)
    """

    viral_units = saan * 12
    scaled = viral_units * 8
    correction = scaled / 40
    net = scaled - correction
    mulam = net / 4.5

    return {
        "saan": saan,
        "viral_units": viral_units,
        "scaled": scaled,
        "correction": correction,
        "net": net,
        "mulam": mulam
    }


# ==========================================================
# TEST BLOCK 
# ==========================================================

if __name__ == "__main__":

    print("UNITS:", list_length_units())

    print("\nTESTS:")
    print("1 அணு → துகள்:", convert_length(1, "அணு", "துகள்"))
    print("1 நெல் → விரல்:", convert_length(1, "நெல்", "விரல்"))
    print("1 சாண் → முழம்:", convert_length(1, "சாண்", "முழம்"))

    print("\nVIRAL SYSTEM:")
    print(list_viral_types())
    print(get_viral_type(8))
    print(viral_to_muzham(9))

    print("15 சாண் → முழம்:", saan_to_mulam(15))
    print("Reverse test:", mulam_to_saan(10))
    print("Debug view:", explain_saan_conversion(15))