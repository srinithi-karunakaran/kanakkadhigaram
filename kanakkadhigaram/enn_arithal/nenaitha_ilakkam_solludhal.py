"""
நினைத்த இலக்கம் சொல்லுதல் - INTERACTIVE GAME ENGINE
====================================================

User performs verse-based arithmetic steps manually.
System reverses the transformation and reveals the hidden number.

====================================================
📜 VERSE LOGIC USED
====================================================

Forward process:
    ×3 → ÷2 → ×3 → ÷2 → −9 → ×4

Reverse process:
    ÷4 → +9 → ×2 → ÷3 → ×2 → ÷3

====================================================
"""


# ==========================================================
# REVERSE ENGINE (CORE LOGIC)
# ==========================================================

def reverse_transform(final_value: float) -> int:
    """
    Reverse the Kanakkadhigaram transformation.

    Parameters
    ----------
    final_value : float
        User's final computed result

    Returns
    -------
    int
        Original hidden number
    """

    step1 = final_value / 4
    step2 = step1 + 9
    step3 = step2 * 2
    step4 = step3 / 3
    step5 = step4 * 2
    step6 = step5 / 3

    return int(step6)


# ==========================================================
# GAME INTERFACE
# ==========================================================

def play_game():
    """
    Interactive Kanakkadhigaram mind-reading game.
    """

    print("\n===== நினைத்த இலக்கம் சொல்லுதல் GAME =====\n")

    print("ஒரு எண்ணை மனதில் நினைக்கவும்.\n")

    print("இப்போது கீழ்கண்ட படிகளை செய்யவும்:\n")
    print("1. எண்ணை 3-ஆல் பெருக்கவும்")
    print("2. 2-ஆல் வகுக்கவும்")
    print("3. மீண்டும் 3-ஆல் பெருக்கவும்")
    print("4. மீண்டும் 2-ஆல் வகுக்கவும்")
    print("5. 9-ஐ கழிக்கவும்")
    print("6. 4-ஆல் பெருக்கவும்\n")

    final = float(input("இறுதியில் கிடைத்த மதிப்பு என்ன?: "))

    original = reverse_transform(final)

    print("\n-----------------------------")
    print(f"🤖 நீங்கள் நினைத்த இலக்கம்: {original}")


# ==========================================================
# RUN
# ==========================================================

if __name__ == "__main__":
    play_game()