"""
யுகம் மற்றும் சகாப்த கணக்கீடு (Yuga & Saka Calendar System)
==========================================================

Ancient Tamil calendrical computation system from Kanakkadhigaram (பாடல்கள் 76–78).

This module includes:
- Kali Yuga year calculation
- Saka Era (Shalivahana) computation
- Historical epoch conversion rules
"""

# ==========================================================
# 1. KALI YUGA SYSTEM (VERSE 76)
# ==========================================================

def kali_yuga_year(saka_year):
    """
    கலியுக ஆண்டு கணக்கீடு

    பாடல் 76:
    கண்டனா டுடனே காலமொரு நூறும்
    தெண்டிரையுந் தில்லை மறையொரு - ஒண்டொடியாய்
    ஒன்பது மாண்டு மோரெழு பதுங்கூட்டி
    நண்பா கலியுக நாள்.

    சக ஆண்டு + 10 + 3000 + 9 + 1 + 70 = கலியுக ஆண்டு

    Simplified formula:
        Kali Yuga = Saka Year + 3180

    Parameters
    ----------
    saka_year : int
        நடப்புக் சக ஆண்டு

    Returns
    -------
    int
        கலியுக ஆண்டு
    """

    return saka_year + 3180


# ==========================================================
# 2. SAKA / SHALIVAHANA ERA (VERSE 77)
# ==========================================================

def saka_year(prabhava_index, current_year):
    """
    சாலிவாகன சகாப்த கணக்கீடு

    பாடல் 77:
    ஐம்பத் தொன்பதுடன் அறுபதை உடன்பெருக்கி
    போன வருடம் புகுவித்து - மானனையாய்
    முன்னூற்று நாற்பதுடன் முப்பத்தையும் கூட்ட
    வென்றாம் சகார்த்தமதே யாம்

    59 × 60 + (பிரபவ முதலான வருட எண்ணிக்கை) + 349

    Simplified form:
        Saka = (59 × 60) + current_cycle + 349

    Parameters
    ----------
    prabhava_index : int
        பிரபவ முதல் நடப்பு வருடம் வரை எண்ணிக்கை

    current_year : int
        ஆண்டு index (cycle adjustment)

    Returns
    -------
    int
        சக ஆண்டு
    """

    return (59 * 60) + prabhava_index + 349


# ==========================================================
# 3. DIRECT FORMULA SYSTEM (VERSE 78)
# ==========================================================

def direct_saka(year_count):
    """
    நேரடி சகாப்த கணக்கீடு

    பாடல் 78:
    அடைந்த இருபதுடன் அறுபதையுந் தான்பெருக்கி
    நடந்த வருவித்ததை நாடி — துடர்ந்து
    ...... சகார்த்தமாங் கலியுக மாமவை
    எண்கலி கூட்ட வந்து.

    60 × 20 + 40 + 349

    Example:
        60 × 20 = 1200
        + 40 years cycle
        + 349 offset

    Parameters
    ----------
    year_count : int
        சுற்று வருட எண்ணிக்கை

    Returns
    -------
    int
        சகாப்த மதிப்பு
    """

    return (60 * 20) + year_count + 349


def kali_from_saka(saka_value):
    """
    சகாப்தத்திலிருந்து கலியுகம் பெறுதல்

    Kali = Saka + 3179 (approx historical mapping)

    Parameters
    ----------
    saka_value : int
        சகாப்த ஆண்டு

    Returns
    -------
    int
        கலியுக ஆண்டு
    """

    return saka_value + 3179


# ==========================================================
# 4. UTILITIES
# ==========================================================

def calendar_summary(saka_year_value):
    """
    முழு காலண்டர் சுருக்கம்

    Returns both:
    - Kali Yuga year
    - Saka year mapping
    """

    return {
        "saka_year": saka_year_value,
        "kali_yuga": kali_yuga_year(saka_year_value)
    }


# ==========================================================
# 5. TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("===== YUGA SYSTEM TEST =====")

    saka = 1589

    print("Saka Year:", saka)
    print("Kali Yuga:", kali_yuga_year(saka))

    print("\nDirect Saka:", direct_saka(40))
    print("Kali from Saka:", kali_from_saka(1589))