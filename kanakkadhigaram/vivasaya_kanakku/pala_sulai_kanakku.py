"""
பலாச்சுளை கணக்கு (Jackfruit Slice Estimation System)
====================================================

Ancient Tamil agricultural estimation method
from Kanakkadhigaram (Verse 89).

Used to estimate number of jackfruit slices
before cutting the fruit.

====================================================
📌 IDEA
====================================================

Estimate slices using:
    (thorn count × 6) ÷ 5
"""


# ==========================================================
# CORE FUNCTION
# ==========================================================

def estimate_jackfruit_slices(thorn_count: int) -> int:
    """
    பாடல் 88 பலாச்சுளை கணக்கு

    தூங்குகின்ற பலாவின் சுளையறிய வேண்டினால்
    ஆங்கிருந்த காம்பின் அருகிருந்த முள்ளெண்ணிப்
    அத்தினால் மாறி அஞ்சினால்
    உள்ளெண்ண வேண்டாஞ் சுளை

    Parameters
    ----------
    thorn_count : int
        Number of small thorns near stem

    Returns
    -------
    int
        Estimated jackfruit slices
    """

    step1 = thorn_count * 6
    step2 = step1 / 5

    return int(step2)


# ==========================================================
# VERSE BREAKDOWN
# ==========================================================

def explain_jackfruit(thorn_count: int):
    """
    Step-by-step verse interpretation
    """

    print("\n===== பலாச்சுளை கணக்கு =====")
    print(f"முள்ளு எண்ணிக்கை = {thorn_count}")

    print("\nகணக்கு படிகள்:")
    print(f"{thorn_count} × 6 = {thorn_count * 6}")
    print(f"{thorn_count * 6} ÷ 5 = {thorn_count * 6 / 5}")


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    print("===== பலாச்சுளை TEST =====\n")

    m = 100

    result = estimate_jackfruit_slices(m)
    print("Estimated slices:", result)

    explain_jackfruit(m)