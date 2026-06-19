from fractions import Fraction

"""
=========================================================
அடிக்கோல் கணக்கீட்டு தொகுப்பு – கணக்கதிகாரம் (135–137)
=========================================================

இது கணக்கதிகாரம் (Kanakkadhigaram) நூலில் வரும்
135 முதல் 137 வரை உள்ள பழந்தமிழ் அளவீட்டு மற்றும்
விகித மாற்றக் கணக்குகளை Python Fraction வடிவில் மாற்றிய தொகுப்பு.

முக்கிய கருத்துகள்:

1. அடிக்கோல் × அடிக்கோல் → பரப்பு கணக்கீடு
2. குறுக்கு பெருக்கல் (cross multiplication)
3. மாகாணி / குழி அளவீட்டு மாற்றம்
4. விகித அடிப்படையிலான மாற்றம்

இந்த module பழந்தமிழ் நில அளவீட்டு கணிதத்தை
நவீன கணக்கீட்டு முறையாக மாற்றுகிறது.
=========================================================
"""


class AdiKolKanakkuSystem:
    """
    கணக்கதிகாரம் verse 135–137 அடிப்படையிலான
    அடிக்கோல் மற்றும் விகித கணக்கீட்டு தொகுப்பு.
    """

    # ---------------------------------------------------------
    def adi_kol_parappu(self, length1, length2, divisor=16):
        """
        பாடல் 135:

        வந்தடி யையுப்பெருக்கி மாகாணி யாக்கியே
        ஒன்பதத் தாறுப் பயனால் — அந்த
        முனிசீர் ராக்கல்ன் காணியாக்கி உடனாக்கி
        பாணன மொழியே பகர்

        பொருள்:
        இரண்டு அடிக்கோல் அளவுகளை பெருக்கி,
        குறிப்பிட்ட divisor மூலம் மாகாணி / குழி கணக்கீடு.

        Parameters:
            length1 (int|float|Fraction):
                முதல் அடிக்கோல் அளவு
            length2 (int|float|Fraction):
                இரண்டாம் அடிக்கோல் அளவு
            divisor (int):
                அளவீட்டு மாற்ற காரணி (default = 16)

        Returns:
            Fraction:
                பரப்பு / குழி மதிப்பு
        """
        return Fraction(length1) * Fraction(length2) / Fraction(divisor)

    # ---------------------------------------------------------
    def kutru_perukkal_maatrangal(self, a, b, divisor=1):
        """
        பாடல் 136

        ஒத்ததொடு கைத்தல மாறி ஒன்றொடே
        கத்தலம் வைத்துகரை காணியாக்கால் — காதலா
        வென்றொன்ற றிக்தே இரண்டிலு மிரத்தே
        பொன்னியந்து கண்டே யுரை

        பொருள்:
        குறுக்கு பெருக்கல் மூலம் அளவீட்டு மாற்றம்.

        Parameters:
            a (int|float|Fraction):
                முதல் மதிப்பு
            b (int|float|Fraction):
                இரண்டாம் மதிப்பு
            divisor (int):
                பகுத்தல் காரணி

        Returns:
            Fraction:
                cross multiplication முடிவு
        """
        return Fraction(a) * Fraction(b) / Fraction(divisor)

    # ---------------------------------------------------------
    def vigitha_maatrangal(self, value, scale_factor):
        """
        பாடல் 137
        
        மாகாணி நிலவு மிக்க விதத்தால்
        கையிறலால் சொல்லுவதெனச் செப்பு

        பொருள்:
        நேரடி விகித மாற்றம் (proportional scaling).

        Parameters:
            value (int|float|Fraction):
                அடிப்படை மதிப்பு
            scale_factor (int|float|Fraction):
                மாற்ற விகிதம்

        Returns:
            Fraction:
                மாற்றப்பட்ட மதிப்பு
        """
        return Fraction(value) * Fraction(scale_factor)


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    obj = AdiKolKanakkuSystem()

    print("\n 135 Output:")
    print(obj.adi_kol_parappu(6, 3))

    print("\n 136 Output:")
    print(obj.kutru_perukkal_maatrangal(12, 8))

    print("\n 137 Output:")
    print(obj.vigitha_maatrangal(10, 2.5))