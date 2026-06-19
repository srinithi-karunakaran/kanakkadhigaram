# ==================================
# எ. கல் கணக்கு (கல் அளவியல்)
# ==================================

def stone_split_volume_ratio(
    base_length=20,
    base_breadth=20,
    base_height=40,
    cut_length=20,
    cut_breadth=10,
    cut_height=4
):
    """
    கணக்கு 209 (எ. கல்)

    அ)
    முறித்தறிய வேண்டியல் முதற்காலால் மாறி
    நிறுத்தியதை நேரிமையாய் நேர்ந்து--முறித்தறிய
    வந்தவகைக் கல்லை முறையால் வருவதற்கு
    முந்தினதிற் கீந்து மொழி.

    கருத்து:
    20×20×40 அளவுள்ள கல்லை
    20×10×4 அளவாக வெட்டினால் எத்தனை துண்டுகள்?

    Parameters
    ----------
    base_length : int
        மூல கல்லின் நீளம்
    base_breadth : int
        மூல கல்லின் அகலம்
    base_height : int
        மூல கல்லின் உயரம்
    cut_length : int
        வெட்டப்பட்ட கல்லின் நீளம்
    cut_breadth : int
        வெட்டப்பட்ட கல்லின் அகலம்
    cut_height : int
        வெட்டப்பட்ட கல்லின் உயரம்

    Returns
    -------
    dict
        துண்டுகளின் எண்ணிக்கை மற்றும் கணக்கீடு விவரம்
    """

    base_volume = base_length * base_breadth * base_height
    cut_volume = cut_length * cut_breadth * cut_height

    pieces = base_volume / cut_volume

    return {
        "மூல_கல்_அளவு": base_volume,
        "வெட்டிய_கல்_அளவு": cut_volume,
        "துண்டுகள்": pieces,
        "விடை": f"{int(pieces)} துண்டுகள்"
    }


# ==================================
# கல் அளவியல் மாற்று கணக்கு (210)
# ==================================

def stone_unit_conversion(
    length_saan=4,
    breadth_saan=2,
    finger_unit=16,
    reduction_factor=8
):
    """
    கணக்கு 210 (எ. கல்)

    அ)
    அகலத்தை நிகளத்தால் மாறி அதனை
    இகலத் தன்னில ரெண்ணவிரலால்--பகருங்கால்
    மாகாணி யிற்றாக்கி மனதுரைக் கால்கழிக்க
    காரணியும் குறையாக் கல்

    கருத்து:
    சாண் அளவுகளை விரல் அளவாக மாற்றி
    பின்னர் மாகாணி/குறுக்கு வகுத்தல் மூலம்
    இறுதி முழ அளவு கண்டறிதல்

    Parameters
    ----------
    length_saan : int
        நீளம் (சாண்)
    breadth_saan : int
        அகலம் (சாண்)
    finger_unit : int
        விரல் அளவு multiplier
    reduction_factor : int
        வகுக்க வேண்டிய காரணி

    Returns
    -------
    dict
        இறுதி முழ அளவு
    """

    base_area = length_saan * breadth_saan
    scaled = base_area * finger_unit
    result = scaled / reduction_factor

    return {
        "அடிப்படை_பரப்பு": base_area,
        "விரல்_மாற்று_அளவு": scaled,
        "இறுதி_முழம்": result,
        "விடை": f"{result} முழம்"
    }


# ==================================
# TEST RUN
# ==================================

if __name__ == "__main__":

    print("=== 209 எ. கல் கணக்கு ===")
    res1 = stone_split_volume_ratio()
    print(res1["விடை"])
    print()

    print("=== 210 எ. கல் கணக்கு ===")
    res2 = stone_unit_conversion()
    print(res2["விடை"])