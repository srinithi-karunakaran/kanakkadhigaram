"""
பின்ன அளவைகள் முறைமை (Fractions & Fine-scale System)

கணக்கதிகாரம் நூலில் உள்ள பாடல்கள் 2 முதல் 15 வரை
எண், நுண் அளவுகள் மற்றும் fractional measurement systems அடிப்படையாகக் கொண்டது.

------------------------------------------------------------

Pinna Alavaigal System

This module implements multiple ancient Tamil fractional and
measurement hierarchies from verses 2-15 of "Kanakkadhigaram".

Systems included:
- Peru En Scale (2-4)
- Saaram Scale (5-8)
- Mundhiri Scale (9-13)
- Kani Scale (14-15)

All systems use a unified hierarchical conversion engine.
"""

# =========================================================
# COMMON ENGINE
# =========================================================

def build_base_values(hierarchy: dict, base_unit: str) -> dict:
    values = {base_unit: 1}
    items = list(hierarchy.items())

    for parent, details in reversed(items):
        child = details["next"]
        factor = details["factor"]
        values[parent] = values[child] * factor

    return values


def convert_system(value, from_unit, to_unit, base_values):
    if from_unit not in base_values:
        raise ValueError(f"Unknown unit: {from_unit}")

    if to_unit not in base_values:
        raise ValueError(f"Unknown unit: {to_unit}")

    value_in_base = value * base_values[from_unit]
    return value_in_base / base_values[to_unit]


# =========================================================
# SYSTEM 1 : PERU EN SCALE (Verses 2–4)
# =========================================================

PERU_EN_HIERARCHY = {
    "கற்பம்": {"next": "புற்புதம்", "factor": 47},
    "புற்புதம்": {"next": "புணரி", "factor": 41},
    "புணரி": {"next": "பற்பம்", "factor": 37},
    "பற்பம்": {"next": "பனிச்சங்கம்", "factor": 33},
    "பனிச்சங்கம்": {"next": "தாய்", "factor": 31},
    "தாய்": {"next": "தந்தை", "factor": 29},
    "தந்தை": {"next": "தனிவருக்கம்", "factor": 27},
    "தனிவருக்கம்": {"next": "முத்தொகை", "factor": 23},
    "முத்தொகை": {"next": "பந்தம்", "factor": 19},
    "பந்தம்": {"next": "சின்னம்", "factor": 17},
    "சின்னம்": {"next": "குணம்", "factor": 15},
    "குணம்": {"next": "சிந்தை", "factor": 3},
    "சிந்தை": {"next": "மும்மி", "factor": 13},
    "மும்மி": {"next": "இம்மி", "factor": 11},
    "இம்மி": {"next": "அணு", "factor": 21}
}

PERU_EN_BASE = build_base_values(PERU_EN_HIERARCHY, "அணு")


def convert_peru_en(value, from_unit, to_unit):
    """
    பாடல் 2
    அற்புத யெண்வாய் தன்னில் தத்தம றாத தெல்லாங்
    கற்புடை மானே கேளு கற்பமே நாற்பத் தேழு
    புற்புதம் நாற்பத் தொன்று புணரியே முப்பத் தேழு
    பற்பமுப் பத்தி மூன்று பனிச்சங்க முப்பத் தொன்றே.

    பாடல் 3
    தாயிருபத் தொன்பது தந்தை யிருபத்தேழு தனிவருக்கம்
    இருபத்தி மூன்று பாயல் முத்தொகை பத்தொன்பது
    பதினைழு பந்தம் பதினைஞ்சு சின்னமாய் குணமும் மூன்று
    சிந்தைபதி மூன்று மும்மி பதினொன்று பாகம் நாலு
    அணிவெளிம்பி இருபத் தொன்றே.

    பாடல் 4
    எண்ணுக்கும் பொன்னுக்கும் முடியும் அதிநுட்பம்
    சின்ன மென்றுபே ராம்.

    Parameters
    ----------
    value : int | float
        மாற்ற வேண்டிய அளவு (Input value)

    from_unit : str
        ஆரம்ப அலகு (Tamil unit name)

    to_unit : str
        இலக்கு அலகு (Target Tamil unit name)

    Returns
    -------
    float
        மாற்றிய மதிப்பு (Converted value)

    """
    return convert_system(value, from_unit, to_unit, PERU_EN_BASE)


def list_peru_en_units():
    return list(PERU_EN_BASE.keys())


# =========================================================
# SYSTEM 2 : SAARAM SCALE (Verses 5–8)
# =========================================================

SAARAM_HIERARCHY = {
    "அதிசாரம்": {"next": "சாரம்", "factor": 45},
    "சாரம்": {"next": "அற்பம்", "factor": 4.5},
    "அற்பம்": {"next": "அதிதற்பரை", "factor": 25},
    "அதிதற்பரை": {"next": "தற்பரை", "factor": 5},
    "தற்பரை": {"next": "அதிநுட்பம்", "factor": 22},
    "அதிநுட்பம்": {"next": "நுட்பம்", "factor": 14},
    "நுட்பம்": {"next": "இம்மி", "factor": 7.5},
    "இம்மி": {"next": "மூன்றாம் கீழ் முந்திரிகை", "factor": 10.5},
    "மூன்றாம் கீழ் முந்திரிகை": {"next": "இரண்டாம் கீழ் முந்திரிகை", "factor": 320},
    "இரண்டாம் கீழ் முந்திரிகை": {"next": "முதலாம் கீழ் முந்திரிகை", "factor": 320},
    "முதலாம் கீழ் முந்திரிகை": {"next": "முந்திரிகை", "factor": 320}
}

SAARAM_BASE = build_base_values(SAARAM_HIERARCHY, "முந்திரிகை")

def convert_saaram(value, from_unit, to_unit):
    """
    பாடல் 5
    ஆனாதி சாரம் நாற்பத் தஞ்சதே சார மாகும்
    தானாதி சாரம் நாலோ டரையதிற் அற்ப மாகும்
    ஊனமில் அதிலற் பந்தான் ஓங்கியவை ஐந்தே யாகில்
    மானிகர் கண்ணாய் அற்பம் எனநீயும் மதித்துச் சொல்லே

    பாடல் 6
    சொல்லிய வற்ப மஞ்சு துய்யதற் பரைத் னக்கு
    வல்லதிங் களுமூன் றென்று வகுத்தற் பரை தாகும்
    நல்லதற் பரையி ரேழு நாடதி நுட்பு மாகும் 
    மெல்லதி நுட்பந் தோறும் ஏழரை நுட்பந் தானே. 

    பாடல் 7
    நுட்பமுன் றரையே யிம்மி நொய்யத் தரையே கொண்டால்
    முட்கரை பெறுக மூன்றுங் கீழின்முந் திரிகை யாகும்
    வடக்கமுந் திரிகை முன்னூற் றிருபதே விரும்பங் காலை 
    புட்செரி சூழாய் இரண்டாய் கீழின்முந் திரிகை யாமே.

    பாடல் 8
    ஆமென இரண்டாய் கீழோர் ஆணிமுத் திரிகை தாகும்
    மாமறை சூழாய் மூன்றாற் றிருபே வினங்குந் தானே
    நாமறை தெரிவு மிக்கோர் பகர்வரே முதற்கீ ழன்றி
    தேமறை தாலு மூன்றாற் றிருபேழுத் திரிகை தானே

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
    return convert_system(value, from_unit, to_unit, SAARAM_BASE)


def list_saaram_units():
    return list(SAARAM_BASE.keys())


# =========================================================
# SYSTEM 3 : MUNDHIRI SCALE (Verses 9–13)
# =========================================================

MUNDHIRI_HIERARCHY = {
    "சின்னம்": {"next": "நுண்மை முந்திரி", "factor": 10.5},
    "நுண்மை முந்திரி": {"next": "இம்மி முந்திரி", "factor": 3},
    "இம்மி முந்திரி": {"next": "கீழ் முந்திரி", "factor": 10.5},
    "கீழ் முந்திரி": {"next": "மேல் முந்திரி", "factor": 320},
    "மேல் முந்திரி": {"next": "ஒன்று", "factor": 320}
}

MUNDHIRI_BASE = build_base_values(MUNDHIRI_HIERARCHY, "ஒன்று")


def convert_mundhiri(value, from_unit, to_unit):
    """
    பாடல் 9
    சின்னம்பத் தேமுக்கால் செப்புந் தொகைநுண்மை
    நுண்மையில் மூன்று நுவல்இம்மி - இம்மி
    இருபத் தரையொன்றாங் கீழாக வேதான்
    வருமுந் திரியெனவே வாட்டு.

    பாடல் 10
    இம்மிதான் ஈரைந் தரையெனவே வைத்ததனைச்
    செம்மைதருங் கீழ்முந் திரிசெய்து - பின்னைவை
    மூன்றுபடி பத்தெட்டி முந்திரியே ஒன்றென்றார்
    ஆன்ற அறிவினவர்.

    பாடல் 11
    இம்மி பத்தரை யென்னா ரிழிவுரைக்க
    செம்மையின்கீழ் முந்திரிகை செப்புங்கால் - நன்மையுடன்
    கேளிர்! சிறுதுகையைக் கேட்டறியச் சொல்லுகிறேன்
    ஆளீர்! கணக்கை அறிந்து.

    பாடல் 12
    இம்மி பத்தரை கீழ்முந் திரியது யெண்ணார்ப்பது
    தும்மிய மேல்முந் திரிகை முன்னூற் றிருபத்தொன்று
    அம்மிய பத்துட னாராயிர மும்பதி னாயிரமும்
    விம்மிய லக்ஷமும் பத்தெலை லக்ஷமும் நூறெனுமே.

    பாடல் 13
    ஒன்றுவ திம்மி ஒருபத் தரைதொண்டால்
    நின்றாடும் கீழ்முந் திரிகையாம் - மொன்றாய்க்கீழ்
    முந்திரிகை முன்னூற் றிருபதே கூடினால்
    வந்துமே முந்திரையென் றோது.

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
    return convert_system(value, from_unit, to_unit, MUNDHIRI_BASE)


def list_mundhiri_units():
    return list(MUNDHIRI_BASE.keys())


# =========================================================
# SYSTEM 4 : KANI SCALE (Verses 14–15)
# =========================================================

KANI_HIERARCHY = {
    "ஒன்று": {"next": "கால்", "factor": 4},
    "கால்": {"next": "மா", "factor": 5},
    "மா": {"next": "காணி", "factor": 4},
    "காணி": {"next": "அரைக்காணி", "factor": 2},
    "அரைக்காணி": {"next": "முந்திரிகை", "factor": 2}
}

KANI_BASE = build_base_values(KANI_HIERARCHY, "முந்திரிகை")


def convert_kani(value, from_unit, to_unit):
    """
    பாடல் 14
    ஒன்றே வரும்வா றுரைப்பதற்கு முந்திரிகை
    நன்றே அரைக்காணி நல்காணி - குன்றாது
    அரைமாவாய் மாவாகிக் கையொரு மாக்காலால்
    திருமாதே நாலொன்றாய்ச் செப்பு.

    பாடல் 15
    முந்திரிய ரைக்காணி முன்னிரண்டு பின்னிரண்டாய்
    வந்ததோர் காணிநான் மாவாக்கி - ஒன்றோடு
    நாலாக்கி காலாக்கி நண்ணுதலாய் காலதனை
    நாலாக்கி ஒன்றாக நாட்டு.

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
    return convert_system(value, from_unit, to_unit, KANI_BASE)


def list_kani_units():
    return list(KANI_BASE.keys())

if __name__ == "__main__":

    print("\n[PERU EN SCALE]")

    print("1 கற்பம் → அணு:")
    print(convert_peru_en(1, "கற்பம்", "அணு"))

    print("10 புணரி → பற்பம்:")
    print(convert_peru_en(10, "புணரி", "பற்பம்"))

    print("Units:")
    print(list_peru_en_units())

    print("\n[SAARAM SCALE]")

    print("1 முந்திரிகை → அதிசாரம்:")
    print(convert_saaram(1, "முந்திரிகை", "அதிசாரம்"))

    print("5 இம்மி → நுட்பம்:")
    print(convert_saaram(5, "இம்மி", "நுட்பம்"))

    print("Units:")
    print(list_saaram_units())

    print("\n[MUNDHIRI SCALE]")

    print("1 மேல் முந்திரி → சின்னம்:")
    print(convert_mundhiri(1, "மேல் முந்திரி", "சின்னம்"))

    print("2 சின்னம் → ஒன்று:")
    print(convert_mundhiri(2, "சின்னம்", "ஒன்று"))

    print("Units:")
    print(list_mundhiri_units())

    print("\n[KANI SCALE]")

    print("1 ஒன்று → முந்திரிகை:")
    print(convert_kani(1, "ஒன்று", "முந்திரிகை"))

    print("1 மா → காணி:")
    print(convert_kani(1, "மா", "காணி"))

    print("Units:")
    print(list_kani_units())