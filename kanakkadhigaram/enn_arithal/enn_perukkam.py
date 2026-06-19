"""
இரட்டிப்பு மற்றும் பெருக்கல் எண்ணியல் முறை (Geometric Growth System)
====================================================================

Ancient Tamil mathematical system from Kanakkadhigaram (பாடல்கள் 79-81).

This module includes:
- Exponential doubling system
- Geometric growth calculations
- Large-scale Tamil number expansion logic
"""

# ==========================================================
# 1. POWER EXPANSION SYSTEM (VERSE 79)
# ==========================================================

def exponential_double(base, times):
    """
    இரட்டிப்பு வளர்ச்சி (2^n system)

    பாடல் 79:
    எட்டெட்டு டரையினெல் லிரட்டித்த லக்கமதை
    இட்டமுள மானே இயம்பிடற் - திட்டமுடன்
    இரண்டை யறுகால் பெருக்கும் இலக்கம்
    திரண்ட கலப்படுத்திச் செப்பு.

    Parameters
    ----------
    base : int
        தொடக்க மதிப்பு (usually 2)

    times : int
        எத்தனை முறை இரட்டிப்பு செய்ய வேண்டும்

    Returns
    -------
    int
        பெருக்கப்பட்ட மதிப்பு
    """

    result = base
    for _ in range(times):
        result *= result
    return result


def lattice_growth(start_value):
    return start_value ** 2


# ==========================================================
# 2. NEL SYSTEM EXPANSION (VERSE 80)
# ==========================================================

def nel_expansion(value):
    """
    நெல் இரட்டிப்பு கணக்கு

    பாடல் 80:
    எட்டேறு பத்துநா லரையா மற்றிநாமே
    இட்டிடங் கொண்டு முதலாக — விட்டிட்டு
    இரட்டித்த நெல்லதனை யீங்குதை ஈதென்றார்
    முரட்டித்த முதறிவி னார்.

    Formula:
        value × 2ⁿ growth pattern

    Parameters
    ----------
    value : int
        நெல் அளவு

    Returns
    -------
    int
        இரட்டிக்கப்பட்ட மதிப்பு
    """

    return value * 2


def recursive_nel(value, depth):
    for _ in range(depth):
        value *= 2
    return value


# ==========================================================
# 3. AREA / SHIFT SYSTEM (VERSE 81)
# ==========================================================

def shift_area(land_value, shift):
    """
    இடமாற்று கணக்கீடு

    பாடல் 81:
    எட்டெட்டு அறுபத்தி நாலுசது ரங்கத்தின்
    முட்டவிடங் கொன்று முதல் கழிந்து — திட்டமாய்
    ஆறுதாங் குழியை அடவுடனே மாறினால்
    வீறாகச் சொல்லலா மே

    Parameters
    ----------
    land_value : int
        நில அளவு

    shift : int
        மாற்ற அளவு

    Returns
    -------
    int
        புதிய மதிப்பு
    """

    return land_value * shift


def reduce_area(value, factor):
    return value / factor


# ==========================================================
# 4. UTILITIES
# ==========================================================

def list_growth_patterns():
    """
    வளர்ச்சி முறை விளக்கம்
    """
    return {
        "doubling": "2^n exponential growth",
        "square": "n² lattice growth",
        "recursive": "multi-step multiplication"
    }


# ==========================================================
# 5. TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("===== GEOMETRIC GROWTH SYSTEM =====")

    print("Square Growth:", lattice_growth(256))
    print("Recursive Nel:", recursive_nel(1, 5))
    print("Shift Area:", shift_area(10, 6))

    print("\nPatterns:")
    print(list_growth_patterns())