from fractions import Fraction

"""
=========================================================
வட்டம் மற்றும் விட்டம் சார்ந்த நில மாற்ற கணக்குகள் (155–158)
=========================================================

இந்த module கணக்கதிகாரம் நூலில் வரும் 155 முதல் 158 வரை உள்ள
விட்டம், வட்டம், இரட்டிப்பு மற்றும் அளவியல் மாற்ற கணக்குகளை
Python Fraction வடிவில் மாற்றுகிறது.

முக்கிய கருத்துகள்:
1. diameter doubling transformation
2. ancient circular approximation (π ≈ 3)
3. multi-stage ratio scaling
4. geometric land transformation

இது பழந்தமிழ் வட்ட கணிதத்தை நவீன கணித வடிவமாக மாற்றுகிறது.
=========================================================
"""


class VattamVithaiNilaKootam:

    # -----------------------------------------------------
    def vitta_irattipu_murai(self, diameter):
        """
        பாடல் 155

        விட்டம் இரட்டித்து வேறந்து கூறிட்டுச்
        சுற்றிய வற்று ளொருமூன்று கூறாக்கி
        விட்டம் இரட்டுமே ஏத்திய வைத்துகை
        வட்டத் தனவும் வகுத்துரைப் போர்க்கே

        பொருள்:
        விட்டத்தை இரட்டித்து பின்னர் விகித அடிப்படையில் பகிர்தல்.

        Refined Logic:
            step1: double diameter
            step2: scale adjustment (÷5)
            step3: weight factor (×3)

        Returns:
            Fraction
        """
        d = Fraction(diameter)
        doubled = d * 2
        return (doubled / 5) * 3

    # -----------------------------------------------------
    def vatta_parappu_kanakku(self, diameter):
        """
        பாடல் 156

        வட்டத் தரைக்கொண்டு வட்டத் தரைமாற
        சட்டெனத் தோன்றுங் குழி.

        பொருள்:
        வட்டத்தின் பரப்பளவு கணக்கீடு.

        Formula:
            π ≈ 3

        Returns:
            Fraction
        """
        r = Fraction(diameter) / 2
        return Fraction(3) * r * r

    # -----------------------------------------------------
    def irattipu_vigitha_murai(self, value, factor):
        """
        பாடல் 157

        விட்ட மிரட்டித்து நால்வட்டத்தை
        எட்டால் ஒத்த வட்டத்தன் வாகுமென்.

        பொருள்:
        இரட்டிப்பு + விகித அடிப்படையிலான மாற்றம்.

        Refined Logic:
            step1: double value
            step2: apply ratio scaling

        Returns:
            Fraction
        """
        v = Fraction(value) * 2
        return v * Fraction(factor)

    # -----------------------------------------------------
    def alaviyal_matrm(self, value, scale):
        """
        பாடல் 158

        விட்டம் மதனை விரைவாய் இரட்டித்து
        மட்டுநான் மாவதனில் மாறியே — எட்டதனில்
        ஏற்றியே செய்யுமிட ஏறுவச் லத்தவும்
        தோற்றுமெனப் புங்கொடி சொன்.

        பொருள்:
        இரட்டிப்பு + அளவியல் மாற்றம்

        Returns:
            Fraction
        """
        v = Fraction(value)
        return v * Fraction(scale)


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    obj = VattamVithaiNilaKootam()

    print("\n155:", obj.vitta_irattipu_murai(10))
    print("156:", obj.vatta_parappu_kanakku(12))
    print("157:", obj.irattipu_vigitha_murai(10, 0.5))
    print("158:", obj.alaviyal_matrm(100, 0.8))