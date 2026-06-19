"""
பூசணி விதை கணக்கு (Pumpkin Seed Estimation System)
==================================================

Ancient Kanakkadhigaram biological estimation method
for calculating seeds inside a pumpkin using ridge counting.


கீற்றெண்ணி முற்றித்துக் கீழறி னாற்பெருக்கி
வேற்றஞ்சு தன்னில் மிகப்பெருக்க
பார்த்ததிலே பாதி யதின்மூன்றில்
மத்தவிதை யாகும் பூசணிக்காய் தோறும் விரை

==================================================
IDEA
==================================================

Two estimation models exist:
1. Multiplicative expansion model
2. Reduction + scaling correction model
"""


# ==========================================================
# MODEL 1 (1350 SEED VERSION)
# ==========================================================

def pumpkin_seed_model_1(ridges: int) -> int:
    """
    பாடல் 86

    கீற்றெண்ணி முற்றித்துக் கீழறி னாற்பெருக்கி
    வேற்றஞ்சு தன்னில் மிகப்பெருக்க
    பார்த்ததிலே பாதி யதின்மூன்றில்
    மத்தவிதை யாகும் பூசணிக்காய் தோறும் விரை

    Parameters
    ----------
    ridges : int
        Number of pumpkin ridges

    Returns
    -------
    int
        Estimated seed count
    """

    step1 = ridges * 3
    step2 = step1 * 6
    step3 = step2 * 5
    step4 = step3 / 2
    step5 = step4 * 3

    return int(step5)


# ==========================================================
# MODEL 2 (900 SEED VERSION)
# ==========================================================

def pumpkin_seed_model_2(ridges: int) -> int:
    """
    பாடல் 86

    கீற்றெண்ணி முற்றித்துக் கீழறி னாற்பெருக்கி
    வேற்றஞ்சு தன்னில் மிகப்பெருக்க
    பார்த்ததிலே பாதி யதின்மூன்றில்
    மத்தவிதை யாகும் பூசணிக்காய் தோறும் விரை

    Parameters
    ----------
    ridges : int
        Number of pumpkin ridges

    Returns
    -------
    int
        Estimated seed count
    """


    step1 = ridges * 3
    step2 = step1 * 4
    step3 = step2 * 5
    step4 = step3 / 2
    step5 = step4 * 3

    return int(step5)


# ==========================================================
# VERSE EXPLANATION
# ==========================================================

def explain_pumpkin(ridges: int):
    """
    Step-by-step breakdown of both traditions
    """

    print("\n===== பூசணி விதை கணக்கு =====")
    print(f"கீற்றுகள் = {ridges}")

    print("\n--- Model 1 (1350 logic) ---")
    print("×3 → ×6 → ×5 → ÷2 → ×3")

    print("\n--- Model 2 (900 logic) ---")
    print("×3 → ×4 → ×5 → ÷2 → ×3")


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    print("===== பூசணி விதை TEST =====\n")

    r = 10

    print("Model 1 output:", pumpkin_seed_model_1(r))
    print("Model 2 output:", pumpkin_seed_model_2(r))

    explain_pumpkin(r)