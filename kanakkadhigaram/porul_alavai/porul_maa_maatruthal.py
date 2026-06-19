"""
பொருள் அளவை - பொது மாற்று செயல்முறை
====================================

This module implements a traditional transformation process:

- One unit is taken as input
- It is divided into four parts
- A transformation rule (Mundhirigai Vaayil) is applied
- A reduction / filtering step is performed
- Final transformed result is produced

No numeric assumptions are included.
"""

# ==========================================================
# PROCESS SIMULATION
# ==========================================================

def porul_maatruthal_process(maa):
    """
    பாடல் 100

    ஒன்றாவது ஒருமாவுக்கு உற்பத் தி யெதன்னில்
    நன்றாக நான்கில் தான்மாறி—குன்றாமல்
    முந்திரிகை வாயில் கழித்து முழுநகையாய்
    இந்தவகை யேதென் றியம்பு.^100ஆ

    பாடல் 101 
    அடிக்கடி தன்னை அறிந்து மாறினால்
    மடித்து தன்னை மாகாணி—யா
    ...... ...... ...... ...... ...... ...... ...... ...... ...... ......
    ...... கழித்திட லொன்றே.^100இ

    பாடல் 102 
    காரி கணக்குமுத லால்தான கோலாகலம்
    சரிவரத் தெளிந்து கொண்டோமென் றேயுலகில்
    குரோதமுட னேவாத்தியார் கோடாலி யென்றபேர்
    மார்பைப் பிளக்குமதுர் மைவச்சிரா யுதமிதே.^100ஈ

    பாடல் 103
     ..... ...... ...... ...... ............ ...... ...... ...... ......
    ...... ...... ...... ...... ...... நுண்னிடையீர்
    பத்திரண்டாஞ் சாண்முழம் பன்னிரு வினாடிகையாம்
    ஒற்றைவினாடி அறுபத் தொன்றே.^100உ

    Parameters
    ----------
    maa : any
        input quantity (symbolic unit)

    Returns
    -------
    dict
        step-by-step transformation trace
    """

    step1 = f"உற்பத்தி: {maa} ஒருமா"

    step2 = "நான்கில் தான்மாறி (4 பகுதிகளாக பிரித்தல்)"

    step3 = "முந்திரிகை வாயில் செயல்முறை பயன்படுத்தப்பட்டது (விதி வரையறுக்கப்படவில்லை)"

    step4 = "கழித்தல் / சுத்திகரிப்பு செய்யப்பட்டது"

    step5 = "முழுநகை வடிவில் இறுதி முடிவு பெறப்பட்டது"

    return {
        "step_1": step1,
        "step_2": step2,
        "step_3": step3,
        "step_4": step4,
        "step_5": step5
    }


# ==========================================================
# HUMAN EXPLANATION
# ==========================================================

def explain_process(maa):
    return f"""
Process Explanation:

- Start: {maa} ஒருமா
- Divide into 4 parts
- Apply transformation rule (not numerically defined)
- Remove / refine intermediate output
- Produce final result

 This is a symbolic process, not a mathematical formula.
"""


# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print("===== PORUL TRANSFORMATION TEST =====\n")

    result = porul_maatruthal_process("1 unit")

    for k, v in result.items():
        print(k, ":", v)

    print("\n--- EXPLANATION ---")
    print(explain_process("1 unit"))