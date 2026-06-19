from fractions import Fraction

"""
=========================================================
பெருங்கோல் அளத்தல் மற்றும் வரி / விகித கணக்குகள் தொகுப்பு
(கணக்கதிகாரம் - பாடல் 127-130 இலிருந்து எடுக்கப்பட்ட கணினி வடிவம்)

Perungol Measurement & Tax-Ratio Computation Module
(Extracted from Kanakkadhigaram - Ancient Tamil Mathematics)
=========================================================

இந்த module பழந்தமிழ் நில அளவீடு, வரி கணக்கீடு,
மற்றும் குறுக்கு விகித கணக்குகளை Python Fraction ஆக மாற்றுகிறது.

முக்கிய கோட்பாடுகள்:
1. நிலம் ↔ குழி மாற்றம்
2. வரி கணக்கீடு (Tax proportional scaling)
3. குறுக்கு பெருக்கல் (Cross multiplication)
4. விகித மாற்றம் (Ratio transformation)
5. inverse proportional கணக்குகள்

This module is a computational translation of ancient Tamil
mathematical verses (Kanakkadhigaram 127–130).
=========================================================
"""


class PerungolKankadhigaram127to130:
    """
    கணக்கதிகாரம் - பாடல் 127 முதல் 130 வரை அடிப்படையாக கொண்ட
    நில அளவீடு மற்றும் வரி கணக்கீட்டு தொகுப்பு.
    """

    # ------------------------------------------------------------
    def land_tax_conversion_verse127(self, land, rate, base):
        """
         பாடல் 127 - பெருங்கோல் அளத்தல் (வரி கணக்கீடு)

        பத்தடி கோல்க டன்னால் அளந்தப் பட்டகொல்லை
        ஒத்திடு மாங்குழி முப்பதுக் சேபன மோர்பனைந்தே
        பற்றிடு மாலிரு பாண்டிக் கோலினிற் பெற்றகொல்லை
        உய்த்திடு மாங்குழி பத்தினுக் செத்தரவெ யோடனமே

        பொருள்:
        நில அளவுக்கு ஏற்ப வரி கணக்கிடுதல்

        Parameters:
            land (int|float): நில அளவு
            rate (int|float): வரி விகிதம்
            base (int|float): அடிப்படை நில அளவு

        Returns:
            Fraction: கணக்கிடப்பட்ட வரி மதிப்பு

        Formula:
            (land × rate) / base
        """
        return Fraction(land) * Fraction(rate) / Fraction(base)

    # ------------------------------------------------------------
    def cross_multiplication_verse128(self, a, b, c):
        """
        பாடல் 128 - குறுக்கு விகித கணக்கீடு

        முன்கோலை மாறியே முன்குழி பெருக்கி முன்னிறைக்கே
        பின்கோ லிறைபண மீவுடன் தாக்கியே பின்றுத்தி
        நன்பான பின்னடிக் கோலக்குழி யாக்கியீய நின்றுணைக்கி
        மூன்றாதி தன்கை யீய்ந்திடக் காணுமிம் முதறிவே.

        பொருள்:
        குறுக்கு பெருக்கல் மூலம் மதிப்பு காணுதல்

        Parameters:
            a (int|float): முதல் மதிப்பு
            b (int|float): இரண்டாம் மதிப்பு
            c (int|float): வகுத்தல் மதிப்பு

        Returns:
            Fraction: குறுக்கு பெருக்கல் முடிவு

        Formula:
            (a × b) / c
        """
        return Fraction(a) * Fraction(b) / Fraction(c)

    # ------------------------------------------------------------
    def inverse_ratio_verse129(self, value, old_ratio, new_ratio):
        """
        பாடல் 129 - விகித மாற்றம்

        ஜவகைக் கதிர் னெல்லை ஐந்தினுக் கீந்து பின்னை
        செவ்வையாய் மாவினாலே சேர்ந்ததோர் பொருளைத் தேர்ந்து
        கைதவ மூன்றில் மாறிக் கழித்தது கலத்திற் கண்டு
        செய்நிலம் நெல்லா தாகச் செப்பிருந் திருந்த வென்றார்.

        பொருள்:
        பழைய விகிதத்திலிருந்து புதிய விகித மாற்றம்

        Parameters:
            value (int|float): அடிப்படை மதிப்பு
            old_ratio (int|float): பழைய விகிதம்
            new_ratio (int|float): புதிய விகிதம்

        Returns:
            Fraction: மாற்றப்பட்ட மதிப்பு

        Formula:
            value × (old_ratio / new_ratio)
        """
        return Fraction(value) * Fraction(old_ratio) / Fraction(new_ratio)

    # ------------------------------------------------------------
    def composite_tax_verse130(self, land, yield_factor, tax_rate, divisor):
        """
        பாடல் 130 - கூட்டுச் கணக்கீடு

        ஊரொன்றில் நாலுகுடி உநிலமும் நாலாறு
        வேலி யிறைநூறு கூறயதால் - பான்மொழியாய்
        ஆறுடனே முக்காலும் அஞ்சேகால் நாலரையும்
        ஏழரையு மாக விளம்பு

        பொருள்:
        நிலம் + விளைச்சல் + வரி இணைந்த கணக்கீடு

        Parameters:
            land (int|float): நில அளவு
            yield_factor (int|float): விளைச்சல் அளவு
            tax_rate (int|float): வரி விகிதம்
            divisor (int|float): வகுத்தல் மதிப்பு

        Returns:
            Fraction: இறுதி கணக்கீடு

        Formula:
            (land × yield × tax_rate) / divisor
        """
        return Fraction(land) * Fraction(yield_factor) * Fraction(tax_rate) / Fraction(divisor)


# ============================================================
# TEST CASES
# ============================================================

if __name__ == "__main__":

    obj = PerungolKankadhigaram127to130()

    print("கணக்கு 127:", obj.land_tax_conversion_verse127(25, 30, 100))

    print("கணக்கு 128:", obj.cross_multiplication_verse128(40, 30, 80))

    print("கணக்கு 129:", obj.inverse_ratio_verse129(100, 3, 4))

    print("கணக்கு 130:", obj.composite_tax_verse130(24, 16, 90, 4))