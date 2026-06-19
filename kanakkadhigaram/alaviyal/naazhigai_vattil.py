"""
நாழிகை வட்டில் (Nazhi Vattil Time Measurement System)
======================================================

Ancient Tamil water-clock based time measurement system
from Kanakkadhigaram (பாடல் 84).

This module describes:
- Water-filled vessel timing method
- Hole size → flow rate → time conversion logic
- Experimental physical time measurement system
"""

# ==========================================================
# SYSTEM CONSTANTS
# ==========================================================

NAZHIGAI_VATTIL = {
    "விரல்_4": 1,
    "விரல்_6": 0.66,
    "விரல்_12": 0.33,
    "விரல்_36": 1  # full vessel reference
}

# ==========================================================
# CORE CONVERSION
# ==========================================================

def vattil_time(finger_width, volume_unit="நாழிகை"):
    """
    பாடல் 84
    மட்டாறு விட்டம் விரலிட்டு வன்செம்பு
    கொட்டார் பதின்பலமாங் கொள்ளுமுளை - கட்டாணி
    நாலெட்டு நான்மாப்பொன் நாலுவிரல் நாழிகையின்
    பால்வட்டிற் பாதிமதிப் பாம்.

    Parameters
    ----------
    finger_width : int | float
        துளை அளவு (விரல் அளவு)

    volume_unit : str
        வெளியீட்டு அலகு (default: நாழிகை)

    Returns
    -------
    float
        ஒரு நாழிகை அளவிற்கு சமமான நேர மதிப்பு
    """

    if finger_width <= 0:
        raise ValueError("Invalid finger width")

    base_rate = 36 / finger_width
    return base_rate


# ==========================================================
# SIMPLE MODEL (FLOW SIMULATION)
# ==========================================================

def simulate_vattil_time(finger_width):
    """
    வட்டில் நீர் சொரிதல் அடிப்படையில் நேரம் கணக்கிடும் முறை
    """

    time = 36 / finger_width
    return round(time, 2)


# ==========================================================
# DISPLAY FUNCTION
# ==========================================================

def display_vattil(finger_width):
    result = simulate_vattil_time(finger_width)
    print(f"{finger_width} விரல் துளை = {result} நாழிகை")


# ==========================================================
# TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("===== NAAZHIGAI VATTIL SYSTEM =====")

    display_vattil(4)
    display_vattil(6)
    display_vattil(19)