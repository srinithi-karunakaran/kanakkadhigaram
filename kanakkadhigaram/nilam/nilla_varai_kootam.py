from fractions import Fraction

"""
=========================================================
நில வரையறை மற்றும் பகிர்வு கணக்குகள் (147–150)
=========================================================

இந்த module கணக்கதிகாரம் நூலில் வரும் 147 முதல் 150 வரை உள்ள
நில அளவீடு, எல்லை சரிசெய்தல், பங்கு பகிர்வு மற்றும் மைய நில
கணக்குகளை Python Fraction வடிவில் மாற்றுகிறது.

முக்கிய கருத்துகள்:
1. எல்லை திருத்தம் (boundary correction)
2. பங்கு அடிப்படையிலான பகிர்வு
3. கலப்பு மதிப்பு (weighted contribution system)
4. மைய நில அளவீடு (central land geometry)

இந்த தொகுப்பு பழந்தமிழ் நில கணிதத்தை நவீன கணித வடிவமாக மாற்றுகிறது.
=========================================================
"""


class NillaVaraiKootam:
    """
    கணக்கதிகாரம் 147–150 நில கணக்கீட்டு தொகுப்பு
    """

    # -----------------------------------------------------
    def ellai_thirutham(self, length, breadth, correction=0.05):
        """
        பாடல் 147:
        கோலடி கோல்குழி யாக்குகழி தனக்கீயந்து
        மாலுடனே யில்வகை சரியாக்கி--கோல
        தொண்டுந் துகை ... ... ... ... ... ...
        ... ... ... ... ... ... 

        பொருள்:
        நிலத்தின் எல்லையில் ஏற்படும் சிறிய பிழைகளை திருத்துதல்.

        Formula (refined):
            (length × breadth) × (1 - correction)

        Returns:
            Fraction
        """
        area = Fraction(length) * Fraction(breadth)
        return area * (1 - Fraction(correction))

    # -----------------------------------------------------
    def pangu_pagalvu(self, total, shares):
        """
        பாடல் 148:

        ஓயாதி யாகவே யொன்பொருளை யீயென்றால்
        ஓவாதிக் கொண்பொன் றுகா--னொவ்வாதே
        உத்தநில மாகவே யொன்பொருளை யீந்தார்க்குப்
        பெத்தபயன் பேர்வழியே பேசு.

        பொருள்:
        பங்குகளின் அடிப்படையில் நியாயமான பகிர்வு.

        Formula:
            (total × share) / sum(shares)

        Returns:
            list[Fraction]
        """
        total = Fraction(total)
        total_share = sum(Fraction(s) for s in shares)

        return [(total * Fraction(s)) / total_share for s in shares]

    # -----------------------------------------------------
    def kalappu_mathippu(self, base, factors):
        """
        பாடல் 149

        பொன்னுக் கினமும் பொருந்துநெல் லுக்கினமும்
        மன்று கடிமை யறுவிடையும் - உன்னி
        அனக்கினமும் கொண்டான் பலமெல்லாம்.....
        வினைக்கும் படியே விளம்பு.

        பொருள்:
        பல காரணிகளை இணைத்து உருவாகும் மதிப்பு.

        Refined Formula:
            base × sum(weighted factors)

        Returns:
            Fraction
        """
        base = Fraction(base)
        return base * sum(Fraction(f) for f in factors)

    # -----------------------------------------------------
    def maiyam_nila_kandam(self, ns, ew):
        """
        பாடல் 150
        
        முச்சதிர மாகில் முறையால் இதையளந்து
        அச்சதிரத் தில்பாதி ஆங்கறிந்து - வச்ச
        ஒருவகையான் மாறி ஓதரிய மேனி
        திருவினையாய் செவ்வனே குழி.

        பொருள்:
        மையத்தை கொண்டு நில பரப்பை கணக்கிடுதல்.

        Formula:
            (ns/2) × (ew/2)

        Returns:
            Fraction
        """
        return (Fraction(ns) / 2) * (Fraction(ew) / 2)


# ==========================================================
#  TEST CASES
# ==========================================================

if __name__ == "__main__":

    obj = NillaVaraiKootam()

    print("\n147:", obj.ellai_thirutham(10, 20))
    print("148:", obj.pangu_pagalvu(100, [1, 2, 3, 4]))
    print("149:", obj.kalappu_mathippu(100, [0.5, 0.25, 0.75]))
    print("150:", obj.maiyam_nila_kandam(20, 30))