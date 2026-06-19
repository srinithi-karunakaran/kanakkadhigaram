"""
=========================================================
சிறுகுழி அளத்தல் (பாடல் 106)
=========================================================

இது Kanakkadhigaram நூலில் உள்ள
“சிறுகுழி அளத்தல்” பகுதியின் கணக்கியல் முறை.

இந்த தொகுதி விளக்கும் விஷயங்கள்:

    - நீளம் × அகலம் மூலம் பரப்பளவு கணக்கிடுதல்
    - 3/4 என்ற பாடல் சார்ந்த திருத்தக் காரணி பயன்படுத்துதல்
    - மாகாணி (16 அலகு) அடிப்படையில் மாற்றுதல்

=========================================================
"""

from fractions import Fraction


class SiruKuzhiAlathal:
    """
    பாடல் 106:

    கல்லுங் குழியுங் கணக்கறிந்து கைநான்குஞ்
    சொல்லும் வகைக்கூட துஞ்சாமல் — மெல்லியலாள்
    அன்னவிற்ப் பாக்கியிய லாக்கிகள விற்கழித்து
    மன்னியமா காணியால் வாட்டு.

    கருத்து:
        - பரப்பளவு = நீளம் × அகலம்
        - திருத்தம் = 3/4
        - மாகாணி = 16 கொண்டு இறுதி அளவு
    """

    CORRECTION_FACTOR = Fraction(3, 4)
    MAGAANI_DIVISOR = 16

    @classmethod
    def area(cls, length: float, width: float) -> float:
        """
         மூல பரப்பளவு

        பாடல்:
            நீளம் × அகலம்

        Parameters:
            length (float): நீளம்
            width (float): அகலம்

        Returns:
            float: பரப்பளவு
        """
        return length * width

    @classmethod
    def apply_correction(cls, area: float) -> float:
        """
        பாடல் 106 படி 3/4 திருத்தம்

        Parameters:
            area (float): பரப்பளவு

        Returns:
            float: திருத்தப்பட்ட பரப்பு
        """
        return area * cls.CORRECTION_FACTOR

    @classmethod
    def to_kuzhi(cls, corrected_area: float) -> float:
        """
         மாகாணி மாற்றம்

        Returns:
            float: இறுதி குழி அளவு
        """
        return corrected_area / cls.MAGAANI_DIVISOR

    @classmethod
    def calculate(cls, length: float, width: float) -> dict:
        """
        முழு சிறுகுழி அளவீடு (பாடல் 106)

        Parameters:
            length (float): நீளம் (உள்ளீடு)
            width (float): அகலம் (உள்ளீடு)

        Returns:
            dict:
                - மூல பரப்பு
                - திருத்தப்பட்ட பரப்பு
                - இறுதி குழி அளவு
        """

        raw = cls.area(length, width)
        corrected = cls.apply_correction(raw)
        kuzhi = cls.to_kuzhi(corrected)

        return {
            "நீளம்": length,
            "அகலம்": width,
            "மூல_பரப்பு": raw,
            "திருத்தப்பட்ட_பரப்பு": float(corrected),
            "சிறுகுழி_அளவு": float(kuzhi)
        }
    
if __name__ == "__main__":

    print("===== சிறுகுழி அளத்தல் (பாடல் 106) =====\n")

    test1 = SiruKuzhiAlathal.calculate(12, 15)
    test2 = SiruKuzhiAlathal.calculate(10, 10)
    test3 = SiruKuzhiAlathal.calculate(20, 5)

    for i, test in enumerate([test1, test2, test3], 1):
        print(f"\n--- Test {i} ---")
        for k, v in test.items():
            print(f"{k} : {v}")