"""
===========================================================
கோல் அளவு கணக்கு (பாடல்கள் 104-105)
===========================================================

இந்த தொகுதி பழமையான தமிழ் அளவியல் முறையில்
கோல் (அளவுக்கோல்) தொடர்பான கணக்குகளை விளக்குகிறது.

பயன்படும் அலகுகள்:
    - முழம் (Muzham)
    - சாண் (Saan)
    - பிடி (Pidi)

அடிப்படை உறவு:
    1 முழம் = 8 சாண்
    1 பிடி = சிறு பகுதி அளவு (சூழ்நிலைக்கு ஏற்ப)

இந்த தொகுதி கோல் அளவின் மாற்றங்களை கணக்கிட பயன்படுகிறது.
===========================================================
"""


class SaanMuzhamConversionSystem:
    """
    பாடல் 104 

    சிறுகோல் முதற்கோல்செம் பாதியிற் பாதி
    நெறியாக சாணிரண்டா மட்டும — செரிமுழலாம்
    நல்லமுழம் ஒன்றின்மேல் சாணும் பிடிகளினு
    சொல்லுவரே வல்லார் துணிந்து

    பாடல் 105 
    முழமும் சாணும் பிடியுங் கொண்டது
    தெளிவுறுங் கோலெனத் தகுமே.

    கருத்து:
    - சிறிய அளவுகள் (சாண், பிடி) கொண்டு முழம் உருவாக்குதல்
    - அளவுகளை மாற்றி கணக்கிடுதல்
    """

    SAAN_PER_MUZHAM = 8

    @classmethod
    def muzham_to_saan(cls, muzham: float) -> float:
        """
        📌 முழத்தை சாணாக மாற்றுதல்

        அளவு:
            muzham (முழம்) -> சாண்

        return:
            சாண் அளவு
        """
        return muzham * cls.SAAN_PER_MUZHAM

    @classmethod
    def saan_to_muzham(cls, saan: float) -> float:
        """
        📌 சாணை முழமாக மாற்றுதல்

        அளவு:
            saan (சாண்)

        return:
            முழம்
        """
        return saan / cls.SAAN_PER_MUZHAM

    @staticmethod
    def half_muzham_in_saan() -> int:
        """
        📌 அரை முழம் எவ்வளவு சாண்?

        return:
            4 சாண்
        """
        return 4

    @staticmethod
    def describe_units() -> dict:
        """
        📌 கோல் அளவின் அலகுகள்

        return:
            அலகுகள் பட்டியல்
        """
        return {
            "அலகுகள்": ["முழம்", "சாண்", "பிடி"],
            "உறவு": "1 முழம் = 8 சாண்"
        }


# ==========================
# TEST (தமிழ் input style)
# ==========================

if __name__ == "__main__":

    print("===== கோல் அளவு கணக்கு (104–105) =====\n")

    # தமிழ் input style
    print("1 முழம் =", SaanMuzhamConversionSystem.muzham_to_saan(1), "சாண்")
    print("8 சாண் =", SaanMuzhamConversionSystem.saan_to_muzham(8), "முழம்")

    print("அரை முழம் =", SaanMuzhamConversionSystem.half_muzham_in_saan(), "சாண்")

    print("\nஅலகுகள்:")
    print(SaanMuzhamConversionSystem.describe_units())