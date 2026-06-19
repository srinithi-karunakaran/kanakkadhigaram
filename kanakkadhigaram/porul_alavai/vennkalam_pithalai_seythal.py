"""
வெண்கலமும் பித்தளையும் செய்தல் (Alloy Mixing System)
=====================================================

Kanakkadhigaram - பாடல் 96

This module converts ancient Tamil material science rules
into modern ratio-based computation.

========================================================
VERSE
========================================================

எட்டெடை செம்பில் இரண்டெடை ஈயமிடில்
திட்டமாய் வெண்கலமாஞ் சேர்த்திருக்கில்
ஏழரையின் முப்பலத் துத்தத்தை யேறியிடத்
தாழ்வரவே பித்தளையாந் தான்

========================================================
MEANING
========================================================

- 8 parts copper + 2 parts tin → Bronze (Venkalam)
- 7.5 parts copper + 3 parts tin → Brass (Pithalai)

========================================================
"""

# ==========================================================
# CORE LOGIC
# ==========================================================

def venkalam_ratio(copper: float) -> dict:
    """
    பாடல் 96 - வெண்கலம் கணக்கு

    Verse:
    ------
    எட்டெடை செம்பில் இரண்டெடை ஈயம்
    → 8:2 ratio

    Parameters
    ----------
    copper : float
        Copper weight

    Returns
    -------
    dict
        Tin required and total alloy
    """

    tin = (2 / 8) * copper
    total = copper + tin

    return {
        "copper": copper,
        "tin": tin,
        "alloy": total
    }


def pithalai_ratio(copper: float) -> dict:
    """
    பாடல் 96 - பித்தளை கணக்கு

    Verse:
    ------
    ஏழரை செம்பில் மூன்று துத்தம்
    → 7.5 : 3 ratio

    Parameters
    ----------
    copper : float

    Returns
    -------
    dict
    """

    tin = (3 / 7.5) * copper
    total = copper + tin

    return {
        "copper": copper,
        "tin": tin,
        "alloy": total
    }


# ==========================================================
# REVERSE CHECK (OPTIONAL FUN MODULE)
# ==========================================================

def identify_metal(copper: float, tin: float) -> str:
    """
    Identify alloy type from ratio
    """

    ratio = tin / copper

    if abs(ratio - 0.25) < 0.01:
        return "வெண்கலம் (Bronze)"
    elif abs(ratio - 0.4) < 0.1:
        return "பித்தளை (Brass)"
    else:
        return "தெரியாத கலவை"


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    print("===== வெண்கலம் / பித்தளை கணக்கு TEST =====\n")

    b = venkalam_ratio(8)
    print("வெண்கலம்:", b)

    p = pithalai_ratio(7.5)
    print("பித்தளை:", p)

    print("\nReverse check:")
    print(identify_metal(8, 2))
    print(identify_metal(7.5, 3))