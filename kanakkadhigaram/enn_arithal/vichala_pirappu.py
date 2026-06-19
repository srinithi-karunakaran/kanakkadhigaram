"""
விசலப்பிறப்பு (Fraction Transformation System - 92 to 95)
==========================================================

Ancient Tamil mathematical system from Kanakkadhigaram.

This module explains fractional transformation logic using
verse-based arithmetic operations such as multiplication,
division, and inverse reconstruction.
"""

# ==========================================================
# CORE FRACTION ENGINE
# ==========================================================

def vichala_transform(n: float) -> float:
    """
    விசலப்பிறப்பு transformation engine (Verse-based logic)

    Verse logic idea:
    -----------------
    ×3 → ÷2 → ×3 → ÷2 → −9 → ×4

    Parameters
    ----------
    n : float
        input number (fractional / integer)

    Returns
    -------
    float
        transformed result
    """

    step1 = n * 3
    step2 = step1 / 2
    step3 = step2 * 3
    step4 = step3 / 2
    step5 = step4 - 9
    step6 = step5 * 4

    return step6


# ==========================================================
# INVERSE CHECK (VALIDATION)
# ==========================================================

def validate_vichala(n: float) -> float:
    return vichala_transform(n)


# ==========================================================
# FRACTION DEMO FUNCTIONS 
# ==========================================================

def fraction_square_34():
    """
    முன்னுரைத்த சொல்லித்தனை முந்தி யாக்கியதன்
    பின்னரைத்த சொல்லுக்குத் தான்மாறி-பின்னுமொரு
    முந்திரிகை வாயில் கழிப்பளவுங் காணுமே
    இத்தர விசலப் பிறப்பு.

    """
    return (3/4) * (3/4)


def fraction_mul_34_316():
    """
    (93) Example: 3/4 × 3/16
    தானினைந்த வாயைச் சதுர்த்தி னால்மாறி
    மானனையாய் காணியால் வாட்டிக்கொள்—யானினைந்த
    சிந்தை யதனாற் திரண்டபொரு ளொன்றுக்கு
    முந்திரிகை வாய்க்கு மொழி

    """
    return (3/4) * (3/16)


def name_based_vichala(name_length: int):
    """
    (94)
    சொன்னான் பேரி லெழுத்தெண்ணித்
    தொகையை இருகால் தான்மாறி
    சொன்னான் பேரி எழுத்துக்கீய
    தோன்றா விசலந் தோன்றுமே.

    Parameters
    ----------
    name_length : int
        number of letters in name

    Returns
    -------
    float
    """
    return (name_length * 3 / 4) * (3 / 4)


def nel_vichala(kalam: float):
    """
    (95) NEL VICHALAM (Rice measure conversion idea)
     நெல்விசலம் வேண்டில் நிறைந்த மரக்காலை
    நல்லதொரு நாழி அதுவாக்கி—சொல்லரிய
    வாயினால் மாறி வரும்பொருள் தன்னை
    இருமா செவிடென் றோது.

    Parameters
    ----------
    kalam : float
        base kalam value

    Returns
    -------
    float
    """
    return kalam * (3/4)


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    print("===== விசலப்பிறப்பு TESTS (92–95) =====\n")

    print("(92) 3/4 × 3/4 =", fraction_square_34())
    print("(93) 3/4 × 3/16 =", fraction_mul_34_316())

    print("(94) name length 4 =", name_based_vichala(4))
    print("(95) kalam 12 → 3/4 =", nel_vichala(12))

    print("\n===== CORE TRANSFORM TEST =====")
    print("Input 10 →", vichala_transform(10))