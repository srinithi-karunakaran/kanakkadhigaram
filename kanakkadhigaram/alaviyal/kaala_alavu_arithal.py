"""கால அளவு அறிதல் (Kaala Alavu Arithal System)
==========================================

கணக்கதிகாரம் நூலில் உள்ள கால அளவீட்டு முறைகளை அடிப்படையாகக் கொண்டு
மிகச் சிறிய நேர அலகுகளிலிருந்து மிகப் பெரிய நேர அலகுகள் வரை
மாற்றும் பாரம்பரிய தமிழ் கணித அமைப்பு இம்மொட்யூலில் செயல்படுத்தப்பட்டுள்ளது.

இதில் உள்ளவை:
- நுண் நேர அளவீட்டு முறை (கண்ணிமை → நாழிகை)
- இரு விதமான பாடல் அடிப்படையிலான hierarchy systems
- பல்வேறு scaling rules (2, 4, 6, 12, 60, 360 etc.)

------------------------------------------------------------

This module implements ancient Tamil time measurement systems
from Kanakkadhigaram.

It includes:
- Micro time unit hierarchy systems
- Multiple poetic rule-based conversions (Verse 35–38)
- Scalable conversion engine using base-value mapping
"""

# ==========================================================
# SYSTEM 35 - MICRO TIME
# ==========================================================

KALA_35 = {
    "கண்ணிமை": 1,
    "கைநொடி": 2,
    "மாத்திரை": 4,
    "குரு": 8,
    "உயிர்": 16,
    "க்ஷணிகம்": 96,
    "வினாடி": 1152,
    "நாழிகை": 69120
}

# ==========================================================
# SYSTEM 36 - INTERMEDIATE TIME
# ==========================================================

KALA_36 = {
    "நாழிகை": 1,
    "வினாடிகை": 60,
    "சூட்சணம்": 720,
    "சூஷ்பிறம்": 2880,
    "கைநொடி": 5760,
    "மாத்திரை": 11520,
    "கண்ணிமை": 23040
}

# ==========================================================
# SYSTEM 37 - CALENDAR TIME
# ==========================================================

KALA_37 = {
    "நாழிகை": 1,
    "சாமம்": 7.5,
    "பொழுது": 30,
    "நாள்": 60,
    "திங்கள்": 1800,
    "வருடம்": 21600
}

# ==========================================================
# SYSTEM 38 - COSMIC / GRANULAR TIME
# ==========================================================

KALA_38 = {
    "கண்ணிமை": 1,
    "கணநேரம்": 4,
    "கட்டடை": 32,
    "மெட்டை": 256,
    "துடி": 1024,
    "மாத்திரை": 4096,
    "வினாடிகை": 1474560,
    "நாழிகை": 88473600
}

# ==========================================================
# SYSTEM REGISTRY
# ==========================================================

SYSTEMS = {
    "micro_time": KALA_35,
    "intermediate": KALA_36,
    "calendar_time": KALA_37,
    "cosmic_time": KALA_38
}

# ==========================================================
# MAIN CONVERTER 
# ==========================================================

def convert_time(value, from_unit, to_unit, system="micro_time"):
    """
    பாடல் 35 
    நிமைநொடி மாத்திரை நிச்சவித் தன்னை
    இமைகுரு பற்றும் உயிரென்றார் - அனையஉயிர்
    ஆறு சணீகமீரா  தாகும் வினாடிதான்
    அறுபத்தே நாழிகை யாம்.

    பாடல் 36:
    கண்ணிமையு மாத்திரையு கைநொடியும் ரண்டாக்கி
    நண்ணிய சூஷ்பிறமும் நாலாகி - எண்ணியிடும்
    பத்திரட்டி சூட்சணமும் பன்னிருவி நாழிகையோ
    டொத்தவி நாடியறுப தேறு.

    பாடல் 37:
    நாழிகை ஏழரை நற்சாமந் தானாலாம்
    போழ்தாகுங் காணாய் பொழுதிரண்டாய்த் - தோழி
    தினமாகி முப்பது திங்களாய்ச் சேர்ந்த
    தினமான தீராறாண் டே.

    பாடல் 38:
    நீளமலர் கற்றெஎன சால நீடுலக்க ... ... ...
    ... ... ... மாமரம் வேயுரு வேண்டில்கணங் கட்டை மெட்டை
    வாழிய துடிதா னாலும் மாத்திரைஆ றறுவ தாகும்
    தாழிய வினாடி துணந்து நாழிகை சென்ற தாமே.

    Parameters
    ----------
    value : float | int
        Input value to convert

    from_unit : str
        Source time unit (Tamil)

    to_unit : str
        Target time unit (Tamil)

    system : str
        Conversion system:
        - micro_time
        - intermediate
        - calendar_time
        - cosmic_time

    Returns
    -------
    float
        Converted value
    """

    if system not in SYSTEMS:
        raise ValueError(f"Unknown system: {system}")

    table = SYSTEMS[system]

    if from_unit not in table:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in table:
        raise ValueError(f"Unknown unit: {to_unit}")

    base = value * table[from_unit]
    return base / table[to_unit]


# ==========================================================
# UTILITIES
# ==========================================================

def list_units(system="micro_time"):
    """Return available units for a system."""
    if system not in SYSTEMS:
        raise ValueError("Unknown system")
    return list(SYSTEMS[system].keys())


def list_systems():
    """Return all supported systems."""
    return list(SYSTEMS.keys())


# ==========================================================
# SIMPLE TEST (optional)
# ==========================================================

if __name__ == "__main__":

    print("SYSTEMS:", list_systems())

    print("\nMICRO TIME TEST")
    print(convert_time(1, "கண்ணிமை", "நாழிகை", system="micro_time"))

    print("\nCALENDAR TIME TEST")
    print(convert_time(1, "நாள்", "வருடம்", system="calendar_time"))

    print("\nCOSMIC TIME TEST")
    print(convert_time(1, "கண்ணிமை", "நாழிகை", system="cosmic_time"))