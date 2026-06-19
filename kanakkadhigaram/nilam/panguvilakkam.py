from fractions import Fraction

"""
=========================================================
பங்கு கணக்கீட்டு தொகுப்பு – கணக்கதிகாரம் (Verse 131–134)
=========================================================

இது கணக்கதிகாரம் (Kanakkadhigaram) நூலில் வரும்
131 முதல் 134 வரை உள்ள பழந்தமிழ் பங்கு பகிர்வு கணக்குகளை
Python Fraction கணக்காக மாற்றிய தொகுப்பு ஆகும்.

இந்த module இல் உள்ள முக்கிய கருத்துகள்:

1. விகித அடிப்படையிலான பங்கு பகிர்வு
2. மொத்த தொகை சார்ந்த சமநிலை கணக்கீடு
3. reciprocal மற்றும் proportional allocation
4. வரி / குத்தகை மாற்று கணக்குகள்
5. பழந்தமிழ் கணித reasoning → computational model

இந்தக் கணக்குகள் அனைத்தும்
பழந்தமிழ் நிலம், பொன், குத்தகை பகிர்வு முறைகளை அடிப்படையாகக் கொண்டவை.
=========================================================
"""


class PanguVilakkamSystem:
    """
    கணக்கதிகாரம் verse 131-134 அடிப்படையிலான பங்கு பகிர்வு கணக்கீட்டு வகுப்பு.
    """

    # ---------------------------------------------------------
    def ur_pangu_pagirkai_(self, pangu_list, motham_panam):
        """
        பாடல் 131
        ஊரொன்றிற் நாலுகுடி உழுதல மும்நான்கு
        ஆறுவேலி யிறைநூறு வந்தக்கால் - கூறில்
        ஆறோடு முக்காலு மஞ்சேகால் நாலரையும்
        ஏழரை மாகு மாம் பங்கு.

        பொருள்:
        6¾, 5¼, 4½, 7½ பங்குகள் கொண்ட நான்கு குடிகளுக்கு
        மொத்த 100 பொன் பகிர்வு.

        Parameters:
            pangu_list (list[Fraction|float]):
                பங்குகள் = [6.75, 5.25, 4.5, 7.5]
            motham_panam (int|float):
                மொத்த பணம் (உதா: 100)

        Returns:
            list[Fraction]:
                ஒவ்வொருவருக்கும் கிடைக்கும் பங்கு
        """
        total = sum(Fraction(x) for x in pangu_list)
        return [(Fraction(x) / total) * motham_panam for x in pangu_list]

    # ---------------------------------------------------------
    def vilai_vigitham_(self, pangu_list, motham_panam):
        """
        பாடல் 132

        குப்பொன்றில் நாலு குடி நாநூறு தாகும்பொன்
        செய்யுமுன் பன்னீது செப்பொன்றால் —
        துப்பவே இரண்டொன்ற மென்னூறு மொள்ளொன்றாய்
        ஆறும் இரண்டொன் பொன்னினைச் செய்தியச் செய்யு

        பொருள்:
        பங்குகளின் reciprocal அடிப்படையில் பகிர்வு மாற்றம்.

        Parameters:
            pangu_list (list): [30, 20, 15, 10]
            motham_panam (int): 75

        Returns:
            list[Fraction]:
                விகித அடிப்படையிலான பகிர்வு
        """
        total = sum(Fraction(x) for x in pangu_list)
        return [(Fraction(x) * motham_panam) / total for x in pangu_list]

    # ---------------------------------------------------------
    def fractional_pangu_(self, pangu_list, motham_panam):
        """
        பாடல் 133

        ஆறில் பாதி யுடையானும் அதனில் பாதி யுடையானும்
        கூரிய நான்கோ லுடையானும் கூறு பெற்ற ஒன்பதுபொன்
        ஏறப் பெற்றோங் குறையாமல், தோயப் பெற்றே மெண்ணாமமல்
        கூறி யாடிதைக் கொடுப்பீராய் குற்ற மற்ற கணக்காமே.

        பொருள்:
        fractional ownership:
            1/2, 1/4, 1/6 அடிப்படையில் பங்கு பகிர்வு

        Parameters:
            pangu_list (list[Fraction]):
                உதா: [1/2, 1/4, 1/6]
            motham_panam (int):
                மொத்த தொகை

        Returns:
            list[Fraction]:
                normalized share distribution
        """
        total = sum(Fraction(x) for x in pangu_list)
        return [(Fraction(x) / total) * motham_panam for x in pangu_list]

    # ---------------------------------------------------------
    def varigal_maatram_(self, theoretical_list, actual_total):
        """
        பாடல் 134:

        நல்ல நிலத்தை நடுவே குழியாக்கி
        கல்விருந்த தாடுதி காணாமல் - சொல்லால்
        இடைவைத்துச் காக்கும் இதுபார்த்தால் தேரே
        கடைவைத்துச் சுற்றாது காண்.

        பொருள்:
        theoretical collection → actual collection scaling

        Parameters:
            theoretical_list (list):
                எதிர்பார்க்கப்பட்ட பங்குகள் (உதா: [30, 20, 15, 10])
            actual_total (int):
                உண்மையான வசூல் (உதா: 60)

        Returns:
            list[Fraction]:
                scaled final distribution
        """
        theoretical_total = sum(Fraction(x) for x in theoretical_list)
        scale = Fraction(actual_total) / theoretical_total
        return [Fraction(x) * scale for x in theoretical_list]


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    obj = PanguVilakkamSystem()

    print("\n131 Output:")
    print(obj.ur_pangu_pagirkai_([6.75, 5.25, 4.5, 7.5], 100))

    print("\n132 Output:")
    print(obj.vilai_vigitham_([30, 20, 15, 10], 75))

    print("\n133 Output:")
    print(obj.fractional_pangu_([1/2, 1/4, 1/6], 9))

    print("\n134 Output:")
    print(obj.varigal_maatram_([30, 20, 15, 10], 60))