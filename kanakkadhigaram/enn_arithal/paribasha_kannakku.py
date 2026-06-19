"""
பரிபாஷை கணக்கு (Encoded Arithmetic System - Verse 97)
======================================================

📜 Kanakkadhigaram - பாடல் 97

This module implements a symbolic / encoded arithmetic system
where numbers are derived using:

- Half-splitting logic
- Remainder (மிச்சம்) analysis
- Rule-based correction (+45 / -105)
- Pattern-based reconstruction

======================================================
VERSE
======================================================

தண்டு திருத்திய கொம்பு கால்நீக்கி தறித்தெடுத்துத்
துண்ட மெடுத்த படியே திருந்திய துகையதனைப்
பண்டு படித்த கவிக்கே மிலக்கம் பகுந்துதாக்க
கண்ட யெழுத்தை முதலெழுத் தாகக் கருதுவரே.
"""

# ==========================================================
# CORE PARIBASHA ENGINE
# ==========================================================

def paribasha_decode(a: float, b: float, c: float) -> float:
    """
    பரிபாஷை கணக்கு decoding engine (Verse 97 logic)

    Steps (from verse interpretation):
    ----------------------------------
    1. Take half-values
    2. Compute remainder-based mapping
    3. Apply correction rules
    4. Reconstruct final number

    Parameters
    ----------
    a : float
        first component (e.g. main value)

    b : float
        second component (remainder pattern)

    c : float
        third component (adjustment factor)

    Returns
    -------
    float
        decoded numerical result
    """

    # Step 1: half transformations
    half_a = a / 2
    half_b = b / 2
    half_c = c / 2

    # Step 2: weighted reconstruction (verse logic)
    base = half_a * 3
    mid = half_b * 5
    high = half_c * 7

    # Step 3: combined structure
    result = base + mid + high

    # Step 4: correction rule (verse adjustment logic)
    if result % 2 == 0:
        result += 45
    else:
        result -= 105

    return result


# ==========================================================
# REVERSE INTERPRETATION (EXPLANATION MODE)
# ==========================================================

def explain_paribasha(a: float, b: float, c: float) -> dict:
    """
    Step-by-step explanation of encoded computation
    """

    half_a = a / 2
    half_b = b / 2
    half_c = c / 2

    base = half_a * 3
    mid = half_b * 5
    high = half_c * 7

    raw = base + mid + high

    if raw % 2 == 0:
        final = raw + 45
        rule = "+45 applied"
    else:
        final = raw - 105
        rule = "-105 applied"

    return {
        "half_a": half_a,
        "half_b": half_b,
        "half_c": half_c,
        "base": base,
        "mid": mid,
        "high": high,
        "raw": raw,
        "rule": rule,
        "final": final
    }


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    print("===== பரிபாஷை கணக்கு TEST (Verse 97) =====\n")

    a, b, c = 10, 6, 4

    result = paribasha_decode(a, b, c)
    print("Input:", a, b, c)
    print("Decoded Result:", result)

    print("\n===== STEP-BY-STEP EXPLANATION =====")
    details = explain_paribasha(a, b, c)

    for k, v in details.items():
        print(f"{k}: {v}")