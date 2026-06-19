"""
எழுத்தாணிக்கு அளவு அறிதல் (Ezhuthanikku Alavu Arithal System)
=============================================================

Ancient Tamil mathematical system from Kanakkadhigaram (பாடல்கள் 70–75).

This module implements:
- Writing instrument measurement system
- Modular arithmetic transformation
- Verse-based numerical reasoning

   பாடல் 70:
   ஓதிய வாயி லுறுவாய்த் துகை தன்னை
   ஆறினால் மாறி யமந்தபொருள் தன்னை
   ஐந்தினா லாய பங்கனைத் தோன்றும்
   இந்த அலகு நிலை

   பாடல் 71:
   மல்லிகை ஐந்து மலர்ந்தபூத் தொண்ணூறு
   கொள்ளுவா ருண்மையாய்ப் பறித்து.

   பாடல் 72:
   பலபரத்து போகுதலகு வாய்பாடு பார்க்க
   இவை தான்கேள் கொடுப்பனவள் வோராண்டுமே காணி
   புலன்கொள்வேள் முழுநிலை வாய்க்கு

   பாடல் 73:
   கோடி மடவார் தங் குன்று போல் மாளிகைமேல்
   பாடல் [பயிலுமிடம்] பத்தொ ருநூ றாயிரமாம் - சேடியர்கள்
   ஐம்பத்தொன் பதினாயிரத்துத் தொளாயிரத்
   தைம்பது மேலாங் கணக்கு.


   பாடல் 74:
   படிக்குமெண் வாய்தன்னில் பார்க்கவே^2 தென்னில்
   தொடிக்கையாய் சொன்னமட் டேத்தி-நொடிப்பளவில்
   ஒன்றுபத் நூறு உகந்ததிலே மாறியே
   வென்றியுடன் சொல்வாய் விரைந்து.

   பாடல் 75:
   ஏழுஞ்ச மூனொன்றும் எட்டாறும் நால்ரெண்டும்
   தாழ்வின்றி யோலைதனித் தான்சேர்த்து - நிழல் சதுரம்
   சகுபிரத மைசஷ்டி சமைந்ததிரி பஞ்சமியும் (திக்குகுலம்)
   அதிர்ந்துதிகை சப்தமியே ஆம்.
"""

# ==========================================================
# CORE FUNCTIONS
# ==========================================================

def ezhuthani_to_value(angulam_length):
    """
   எழுத்தாணி அளவு → லக்கம் மாற்றம

   அங்குல அளவை ஆறால் பெருக்கி "லக்கம்" ஆக மாற்றுதல்.

    Parameters
    ----------
    angulam_length : int | float
        எழுத்தாணியின் அங்குல அளவு

    Returns
    -------
    int | float
        லக்கம் மதிப்பு (angulam × 6)
    """
    return angulam_length * 6


def lakkam_remainder(lakkam_value):
    """
    லக்கம் மதிப்பில் 7-ஆல் வகுத்து மீதி காணுதல்

    பாடல் 70-74:
    எண்ணை 7-ஆல் வகுத்து மீதியை அடிப்படையாகக் கொண்டு முடிவு செய்யப்படுகிறது.

    Parameters
    ----------
    lakkam_value : int | float
        லக்கம் மதிப்பு

    Returns
    -------
    int
        மீதி (mod 7)
    """
    return lakkam_value % 7


def classify_remainder(rem):
    """
    மீதி அடிப்படையில் விளக்கம் வழங்குதல்

    பாடல் 70-74:

    1 → பெண் சாதி மரணம்  
    2 → அறச்செயல் குறைவு  
    3 → நோய் நிலை  
    4 → அரை அதிகாரம்  
    5 → மகாசுகம்  
    6 → விபத்து நீக்கம்  
    0 → மரணம்  

    Parameters
    ----------
    rem : int
        7-ஆல் வகுத்த மீதி

    Returns
    -------
    str
        பொருத்தமான விளக்கம்
    """

    mapping = {
        1: "பெண் சாதி மரணம்",
        2: "அறச்செயல் குறைவு",
        3: "ரோக நிலை",
        4: "அரை அதிகாரம்",
        5: "மகாசுகம்",
        6: "விபத்து நீக்கம்",
        0: "மரணம்"
    }

    return mapping.get(rem, "தெரியாத நிலை")


def compute_vayil(base, multiplier):
    """
    எண் வாய் கணக்கு (Verse 70-74 சூத்திரம்)

    பாடல்:
    எண்ணை 6-ஆல் பெருக்கி பின்னர் 5-ஆல் கழித்தல்.

    Formula:
        result = (base × multiplier × 6) - (base × multiplier × 5)

    Parameters
    ----------
    base : int | float
        அடிப்படை மதிப்பு

    multiplier : int | float
        பெருக்கி

    Returns
    -------
    int | float
        கணக்கிடப்பட்ட மதிப்பு
    """

    step = base * multiplier
    return (step * 6) - (step * 5)


# ==========================================================
# MAIN PIPELINE
# ==========================================================

def analyze_ezhuthani(angulam):
    """
    முழு எழுத்தாணி கணக்கு அமைப்பு

    Steps:
    1. அங்குலம் → லக்கம்
    2. லக்கம் → 7-ஆல் மீதி
    3. மீதி → பொருள் விளக்கம்

    Parameters
    ----------
    angulam : int | float
        எழுத்தாணி அங்குல அளவு

    Returns
    -------
    dict
        {
            "angulam": input value,
            "lakkam": converted value,
            "remainder": mod result,
            "meaning": interpretation
        }
    """

    lakkam = ezhuthani_to_value(angulam)
    rem = lakkam_remainder(lakkam)
    meaning = classify_remainder(rem)

    return {
        "angulam": angulam,
        "lakkam": lakkam,
        "remainder": rem,
        "meaning": meaning
    }


# ==========================================================
# UTILITIES
# ==========================================================

def list_meanings():
    return {
        1: "பெண் சாதி மரணம்",
        2: "அறச்செயல் குறைவு",
        3: "ரோக நிலை",
        4: "அரை அதிகாரம்",
        5: "மகாசுகம்",
        6: "விபத்து நீக்கம்",
        0: "மரணம்"
    }


# ==========================================================
# TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("===== எழுத்தாணி கணக்கு =====")

    result = analyze_ezhuthani(10)

    print("அங்குலம்:", result["angulam"])
    print("லக்கம்:", result["lakkam"])
    print("மீதி:", result["remainder"])
    print("விளக்கம்:", result["meaning"])

    print("\nமீதி விளக்கங்கள்:")
    print(list_meanings())