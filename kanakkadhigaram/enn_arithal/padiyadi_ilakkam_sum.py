"""
படியடி இலக்கம் காணல் (Verse 87 - Arithmetic Series System)
==========================================================

Ancient Tamil Kanakkadhigaram method to compute:

    1 + 2 + 3 + ... + n

based on pairing and midpoint logic.

==========================================================
IDEA
==========================================================

Sum = (n / 2) × (n + 1)
"""


# ==========================================================
# CORE FUNCTION
# ==========================================================

def sum_of_natural_numbers(n: int) -> int:
    """
    பாடல் 87:
    ஒன்றா யொருபத் தொருநூத் தாயிரமாய்
    நின்றபதி னாயிரமாய் நேரே — குன்றாமல்
    பாதியாய் நின்ற தொகைக்குப்பய னெண்ணுடனே
    ஆதியாய்ப் பெருக்கி அறி. 

    - பாதி (n/2)
    - முதல் + கடைசி (1 + n)
    - பெருக்கல்

    Parameters
    ----------
    n : int
        Last number in sequence

    Returns
    -------
    int
        Sum from 1 to n
    """

    return int((n / 2) * (n + 1))


# ==========================================================
# VERSE-STYLE BREAKDOWN
# ==========================================================

def explain_sum(n: int):
    half = n / 2
    pair = n + 1
    result = half * pair

    print("\n===== VERSE BREAKDOWN =====")
    print(f"n = {n}")
    print(f"பாதி (n/2) = {half}")
    print(f"முதல் + கடைசி (n+1) = {pair}")
    print(f"பெருக்கல் = {result}")


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    print("===== படியடி இலக்கம் காணல் TESTS =====\n")

    for n in [10, 20, 50, 60, 100]:

        result = sum_of_natural_numbers(n)
        print(f"1 → {n} = {result}")

    explain_sum(10)