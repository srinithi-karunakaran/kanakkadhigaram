"""
பொருள் அளவை அறிதல் (Verse 99 - PURE LOGICAL MODEL)
===================================================

📜 Kanakkadhigaram - பாடல் 99

This version does NOT invent numeric factors.
It only models the PROCESS described in the verse:

- Go to sea
- Collect water (நாழி மோந்து)
- Observe / analyze
- Identify salt (உப்பு)
- Return interpretation

No artificial multipliers are used.
"""

# ==========================================================
# 1. PURE VERSE PROCESS MODEL
# ==========================================================

def sea_salt_observation(nazhi):
    """
    Verse-based process simulation (no invented math)

    Parameters
    ----------
    nazhi : any
        symbolic quantity of sea water

    Returns
    -------
    dict
        observational result only
    """

    return {
        "step_1": "கடலிற் சென்று நீர் எடுத்தல்",
        "step_2": f"{nazhi} நாழி நீர் சேகரிக்கப்பட்டது",
        "step_3": "நீரை ஆய்வு செய்தல்",
        "step_4": "உப்பு இருப்பது கண்டறியப்பட்டது",
        "step_5": "அளவு பற்றி முடிவு கேட்கப்படுகிறது"
    }


# ==========================================================
# 2. INTERPRETATION FUNCTION (HUMAN READABLE)
# ==========================================================

def explain_verse_99(nazhi):
    """
    Human explanation of verse process
    """

    return f"""
Verse 99 Process:

1. Sea is visited
2. Water collected: {nazhi} நாழி
3. Observation done
4. Salt identified in sea water
5. Question: "How much salt is in this sea water?"

--No numeric formula is given in the verse.
"""


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print("===== VERSE 99 PURE MODEL =====\n")

    result = sea_salt_observation(10)
    for k, v in result.items():
        print(k, ":", v)

    print("\n--- EXPLANATION ---")
    print(explain_verse_99(10))