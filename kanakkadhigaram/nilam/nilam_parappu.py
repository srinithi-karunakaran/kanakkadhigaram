"""
நிலப்பரப்பு கணக்கு (Nilam Parappu System)
=========================================

கணக்கதிகாரம் பாடல் 47 அடிப்படையில் நிலத்தின் பரப்பளவு கணக்கீடு.

This module implements land area calculations based on
ancient Tamil measurement concepts from Kanakkadhigaram.

It includes:
- Basic land area computation
- Future support for Tamil land unit conversions
"""

# ==========================================================
# CORE FUNCTION
# ==========================================================

def calculate_land_parappu(length, width):
    """
    பாடல் 47
    வாசிறு விறற்கு பூமி வருவது தன்னில் மாறி
    ஓசைமா காணி யாக்கி ஒன்பதுக் கீய்ந்து அஞ்சு
    மாசற மாறி முந்தை வருநில வழிசாண் தன்னை
    நேசமாங் காணி யாக்கி நின்றதை மாற பூமி.

    Parameters
    ----------
    length : float | int
        நிலத்தின் நீளம்

    width : float | int
        நிலத்தின் அகலம்

    Returns
    -------
    float
        பரப்பளவு (square units)
    """
    return length * width


# ==========================================================
# OPTIONAL UTILITIES
# ==========================================================

def get_land_area(length, width):
    """Alias for calculate_land_parappu"""
    return calculate_land_parappu(length, width)

# ==========================================================
# TEST 
# ==========================================================

if __name__ == "__main__":
    print("=== LAND AREA TEST ===")
    print("Area:", calculate_land_parappu(10, 5))
    print("Area:", calculate_land_parappu(20, 12))