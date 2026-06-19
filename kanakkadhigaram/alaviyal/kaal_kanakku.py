# ==============================
# உ. கால் கணக்கு (205–207)
# ==============================


def kal_money_ratio_conversion(
    base_nazhi: float = 8,
    base_kalam: float = 80,
    base_money: float = 14,
    target_nazhi: float = 9,
    target_kalam: float = 50
):
    """
    205 கணக்கு (கால் கணக்கு - பணம் விகித மாற்றம்)

    Verse:
    ஆதியுட னாறாய் அமர்ந்ததனை அஞ்சாமல்
    நீதியுடன் கால்தன்னை நேர்மாறி—மாதே
    இரண்டுமுதல் ஐந்தளவும் ஏற்றமாய் மாறித்
    திரண்டதனை யீந்தவர்க்குச் செப்பு.

    Problem Idea:
    If price depends on (nazhi × kalam),
    then money changes proportionally.

    Parameters:
    base_nazhi (float): reference nazhi value
    base_kalam (float): reference kalam value
    base_money (float): reference money value
    target_nazhi (float): new nazhi value
    target_kalam (float): new kalam value

    Returns:
    float: calculated money for target condition
    """
    result = (target_nazhi * target_kalam * base_money) / (base_nazhi * base_kalam)
    return round(result, 6)


def kal_inverse_scale_conversion(
    total_kalam: float = 900,
    old_unit: float = 8,
    new_unit: float = 7
):
    """
    206 கணக்கு (மாற்று அளவீடு - inverse scaling)

    Verse:
    ஒன்றுடன் ரெண்டு மாறி யுய்ந்ததா யிந்தப்
    பின்னும்முன் வந்தவற்றை மூன்று னாலில் பெருக்கிப்
    பொன்னுதனதனை மாறிப் பதப்படும் பொருளின் முன்பே
    நின்றதற் கந்த பேரு நெல்லென சொல்லு நீயே.

    Idea:
    Quantity is inversely proportional to measuring unit.

    Parameters:
    total_kalam (float): known measured quantity
    old_unit (float): old measuring scale
    new_unit (float): new measuring scale

    Returns:
    float: converted quantity in new scale
    """
    result = (total_kalam * old_unit) / new_unit
    return round(result, 6)


def kal_combined_vessel_output(
    vessel_sizes=None,
    base_kalam: float = 8,
    base_output: float = 100
):
    """
    207 கணக்கு (பல கால் சேர்க்கை கணக்கு)

    Verse:
    கால்களெல்லாங் கூட்டிக் கடுகி யளக்கையிலே
    மேல்கொள்வகை வேண்டி வினவினால்--கால் கொள்ளப்
    பெற்றநெல்லைக் காலாலே மாறிப் பிறழாமல்
    உற்றதொகைக்கீந்தே உரை.

    Idea:
    Total output depends on sum of vessel sizes.

    Parameters:
    vessel_sizes (list): list of kal values
    base_kalam (float): reference kal
    base_output (float): reference output

    Returns:
    float: combined output value
    """
    if vessel_sizes is None:
        vessel_sizes = [6, 7, 8, 9, 10]

    total = sum(vessel_sizes)
    result = (total * base_output) / base_kalam
    return round(result, 6)


# ==============================
# TEST RUN
# ==============================

if __name__ == "__main__":
    print("=== உ. கால் கணக்கு TEST ===\n")

    print("Result:", kal_money_ratio_conversion(
        base_nazhi=8, base_kalam=80, base_money=14,
        target_nazhi=9, target_kalam=50
    ))

    print("Result:", kal_inverse_scale_conversion(
        total_kalam=900, old_unit=8, new_unit=7
    ))

    print("Result:", kal_combined_vessel_output(
        vessel_sizes=[6, 7, 8, 9, 10],
        base_kalam=8,
        base_output=100
    ))