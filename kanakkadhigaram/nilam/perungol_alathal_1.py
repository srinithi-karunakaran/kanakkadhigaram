from fractions import Fraction

"""
=========================================================
பெருங்கோல் அளத்தல் மற்றும் விகித கணக்குகள் தொகுப்பு
(கணக்கதிகாரம் – பழந்தமிழ் கணித நூலிலிருந்து எடுக்கப்பட்ட வடிவம்)

Perungol Measurement and Ratio Computation Module
(Extracted from Kanakkadhigaram – Ancient Tamil Mathematics)

இந்த module பழந்தமிழ் நில அளவீட்டு கணக்குகளை
Python Fraction arithmetic ஆக மாற்றுகிறது.

Core Concepts:
- நில பரப்பளவு (area) கணக்குகள்
- விகித (ratio) மாற்றங்கள்
- குறுக்கு பெருக்கல் (cross multiplication)
- பகுத்தல் மற்றும் fractional scaling
- inverse proportional transformations

This module is a computational representation of ancient Tamil
mathematical land measurement techniques described in Kanakkadhigaram.

        பாடல் 119
        அடிக்கடிகை மாறி குழியறிய வேண்டில்
        அடிக்கடியே அவ்வடியை மாறி — வடுக்கண்ணாய்
        மாகாணி யில்தாக்கி யொன்பதின்மாக் கீழ்தாக்கால்
        காகாணி குன்றாது காண்.

        பாடல் 120
        கோலென வறியாத குழிதலக் கீந்து
        வாரிய பல வாரிய பலத்தை - வருகிக்சு
        மூளஞ் செய்ய சீரி ......
        சிறந்துடன் தோன்றுங் குழி.

         பாடல் 121
        ஒதகை நிலமாக்கி உத்தநிலந் தன்னை
        வருசையுடன் தாக்கி வைத்திறாய் - பொருவழி சேர்
        கணங்குழலாய் கனிந்த மென்முலையாய் என்றாய்
        நிலைநாற் செந்தே னே.
        
        பாடல் 122
        முன்னடி கோலின் தாக்கைப் பின்னிடி கையி லீந்து
        முன்னூறு குழிக்கு மாறி பின்னூறு குழியாய் வைத்துப்
        பொன்னொடு மூவி லக்கப் பேரான கடையி (டையில்) மாறிக்
        காணமுந்தி யான பொன்னாம் தன்னா னைந்துகை கணக்கே

        பாடல் 124
        கடையுந் தலையுங் கருதியே தாக்கி
        வடிவுடைய மாதே வகுக்கில் — இடைதனக்
        கீந்து பெரும்பயனே பொன்னளி றுப்பார்க்கு
        வாய்த்தநில மாகும் வகை.

        பாடல் 125
        அந்தமு மாதியு மோரினமே யாமாகித்
        சந்தனையுந் தம்பியையுந் தாக்கியபின் — முந்தவே
        பெற்ற பயனைப் பிழையா லீந்ததுவே
        பொற்கொடியாய் நீயிருக்கும் பொன்

        பாடல் 126
        நன்னிலத்தில் நட்டமுடி நாநூறு மாமதனில்
        எண்ணுமுடி யொன்றில் முதல் எண்ணான்காம் — ஒன்று முதல்
        மண்ணுறவே யோங்கி வளர்ந்தகதிர் எட்டதனில்
        தொண்ணூறு நெற்கதிர்க்குச் சொல்
=========================================================
"""


class PerungolAlathal:
    """
    Kanakkadhigaram based Perungol measurement system.

    This class implements land measurement, ratio scaling,
    cross multiplication and fractional transformation methods
    derived from ancient Tamil mathematical verses.
    """

    # -------------------------------------------------
    def land_area_product(self, side1, side2):
        """

        Parameters:
            side1 (float|int): First land measurement
            side2 (float|int): Second land measurement

        Returns:
            Fraction: Product of land dimensions

        Explanation:
            Two land sides are multiplied to compute area.
        """
        return Fraction(side1) * Fraction(side2)

    # -------------------------------------------------
    def fractional_land_division(self, value, divisor):
        """

        Parameters:
            value (float|int): Base land value
            divisor (Fraction|str): Fractional divisor

        Returns:
            Fraction: Divided and scaled result

        Explanation:
            Value is divided using fractional composition.
        """
        return Fraction(value) / Fraction(divisor)

    # -------------------------------------------------
    def ratio_conversion(self, value, a, b):
        """

        Parameters:
            value (float|int): Base value
            a (float|int): New ratio numerator
            b (float|int): Old ratio denominator

        Returns:
            Fraction: Ratio converted value

        Explanation:
            Applies proportional scaling (a / b)
        """
        return Fraction(value) * Fraction(a, b)

    # -------------------------------------------------
    def cross_multiplication(self, x1, y1, x2):
        """

        Parameters:
            x1 (float|int): Base reference
            y1 (float|int): Known value
            x2 (float|int): New reference

        Returns:
            Fraction: Cross multiplied result

        Explanation:
            Computes y2 = (x2 × y1) / x1
        """
        return Fraction(x2 * y1, x1)

    # -------------------------------------------------
    def chained_ratio_product(self, base, ratios):
        """

        Parameters:
            base (float|int): Initial value
            ratios (list): List of ratios

        Returns:
            Fraction: Final chained result

        Explanation:
            Sequential multiplication of ratios.
        """
        result = Fraction(base)
        for r in ratios:
            result *= Fraction(r)
        return result

    # -------------------------------------------------
    def inverse_ratio_conversion(self, value, a, b):
        """

        Parameters:
            value (float|int): Base value
            a (float|int): Direct scale
            b (float|int): Inverse scale

        Returns:
            Fraction: Inversely scaled value

        Explanation:
            value × (b / a)
        """
        return Fraction(value) * Fraction(b, a)


# ============================================================
# TEST CASES
# ============================================================

if __name__ == "__main__":

    obj = PerungolAlathal()

    print("Test 1:", obj.land_area_product(45, 60))

    print("Test 2:", obj.fractional_land_division(
        2925, Fraction(3, 4) + Fraction(3, 16)
    ))

    print("Test 3:", obj.ratio_conversion(100, 3, 4))

    print("Test 4:", obj.cross_multiplication(12, 100, 16))

    print("Test 5:", obj.chained_ratio_product(10, ["1/4", "1/2", "3/5"]))

    print("Test 6:", obj.inverse_ratio_conversion(100, 3, 4))