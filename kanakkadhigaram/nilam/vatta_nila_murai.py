from fractions import Fraction

"""
=========================================================
வட்ட நில கணக்குகள் – இறுதி தொகுதி (159–160)
=========================================================

இந்த module கணக்கதிகாரம் நூலில் வரும் இறுதி 159–160 பாடல்களின்
வட்ட நில அளவீடு மற்றும் இணைந்த சுற்றளவு-விட்டம் கணக்குகளை
Python Fraction வடிவில் மாற்றுகிறது.

முக்கிய கருத்துகள்:
1. ancient circle approximation (π ≈ 3)
2. diameter-radius transformation
3. circumference reduction logic
4. combined geometric land computation

இது பழந்தமிழ் geometry கணக்குகளின் இறுதி வடிவமாகும்.
=========================================================
"""


class VattamKootalNilaMurai:

    # -----------------------------------------------------
    def vatta_nila_parappu(self, diameter):
        """
        பாடல் 159

        வட்டத் தரைக்கொண்டு வட்டத் தரைமாறக்
        கட்டேற விளங்கும் குழி.

        பொருள்:
        வட்ட நில பரப்பு கணக்கீடு

        Formula:
            π ≈ 3

        Returns:
            Fraction
        """
        d = Fraction(diameter)
        r = d / 2
        return Fraction(3) * r * r

    # -----------------------------------------------------
    def kootiya_vatta_nila(self, circumference, diameter):
        """
        பாடல் 160:
        
        வட்டத் தரையே வரையவோர் மாவும்
        வட்டத்தைக் கொண்டுவிரித் துக்கோள்ள - வட்டம்
        அரையேவொரு மாவுமறு மாகாணி யிற்பெருக்கி
        தெரிந்தகுழி யீதெனச் செப்பு.

        பொருள்:
        சுற்றளவு மற்றும் விட்டத்தை குறைத்து
        இணைந்த நில கணக்கு

        Refined Logic:
            step1: reduce circumference → half
            step2: reduce diameter → half
            step3: multiply reduced values

        Returns:
            Fraction
        """
        c = Fraction(circumference) / 2
        d = Fraction(diameter) / 2
        return c * d


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    obj = VattamKootalNilaMurai()

    print("\n159:", obj.vatta_nila_parappu(12))
    print("160:", obj.kootiya_vatta_nila(40, 12))