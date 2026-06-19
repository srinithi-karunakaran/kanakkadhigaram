from fractions import Fraction

"""
=========================================================
கர்ணம் மற்றும் வட்ட நில அளவீட்டு கணக்குகள் (151–154)
=========================================================

இந்த module கணக்கதிகாரம் நூலில் வரும் 151–154 பாடல்களின்
கர்ண அடிப்படையிலான நில கணக்குகள், மூவகை நில பகிர்வு,
விகித கணக்குகள் மற்றும் வட்ட நில அளவீடுகளை Python Fraction
வடிவில் மாற்றுகிறது.

முக்கிய கருத்துகள்:
1. diagonal-based land computation
2. geometric partition logic
3. proportional scaling
4. circular approximation methods

இது பழந்தமிழ் geometry + land calculation முறைகளை
நவீன கணித வடிவமாக மாற்றுகிறது.
=========================================================
"""


class KarnaVattaNilaKootam:

    # -----------------------------------------------------
    def karna_adippadai_kandam(self, sides):
        """
        பாடல் 151
        
        கர்ணத்தில் பாதி பாதியா லாக்கி
        முன்னின்றி யொக்குங் குழி.

        பொருள்:
        பல பக்க நிலங்களை கர்ண அடிப்படையில் சமநிலைப்படுத்துதல்.

        Refined Logic:
            sum(sides) → diagonal weight → scaled half

        Returns:
            Fraction
        """
        total = sum(Fraction(s) for s in sides)
        return (total / 2) * Fraction(5, 1)

    # -----------------------------------------------------
    def mukkona_nila_pirivu(self, base, height):
        """
        பாடல் 152

        இரண்டும் தலையும் நடுவுமுன்னே பாதியாக்கி
        ஒன்றோடொன்று மாறிக் குழி.

        பொருள்:
        மூவகை நிலத்தை சமநிலைப்படுத்தும் மாற்று கணக்கு.

        Refined Logic:
            normalized geometric split

        Returns:
            Fraction
        """
        return (Fraction(base) * Fraction(height)) / 2

    # -----------------------------------------------------
    def pagupadu_nila(self, total_land, share):
        """
        பாடல் 153

        குணங்கொண்டு கோலால் குழியுரைப்ப தன்றி
        இணங்கும் வகைபரிதாம் என்று

        பொருள்:
        பங்கு அடிப்படையிலான நில பகிர்வு.

        Formula:
            total × share

        Returns:
            Fraction
        """
        return Fraction(total_land) * Fraction(share)

    # -----------------------------------------------------
    def vatta_nila_kanakku(self, radius):
        """
        பாடல் 154:

        வட்டத் தரைக்கொண்டு வட்டத் தரைமாறப்
        பட்டத் திருக்குணத் தான்பகரில் — நிட்ட
        இருகையால் பாதி யுடனே யதிபாதி
        மருவளரும் பூங்குழலே மாறு.

        பொருள்:
        வட்ட நில அளவீடு (approximation model)

        Refined Formula:
            3 × r²

        Returns:
            Fraction
        """
        r = Fraction(radius)
        return Fraction(3) * r * r


# ==========================================================
# 🧪 PYPI TEST CASES
# ==========================================================

if __name__ == "__main__":

    obj = KarnaVattaNilaKootam()

    print("\n151:", obj.karna_adippadai_kandam([10, 8, 12]))
    print("152:", obj.mukkona_nila_pirivu(10, 20))
    print("153:", obj.pagupadu_nila(100, 0.25))
    print("154:", obj.vatta_nila_kanakku(10))