from fractions import Fraction

"""
=========================================================
நில கணக்கீட்டு மாற்றங்கள் – கணக்கதிகாரம் (138–146)
=========================================================

இந்த module கணக்கதிகாரம் நூலில் வரும் 138–146 பாடல்களின்
நில அளவீட்டு, விகித மாற்றம், திருத்த கணக்குகளை Python Fraction
முறையில் மாற்றுகிறது.

முக்கிய கருத்துகள்:
1. fractional correction (சிறிய திருத்தங்கள்)
2. geometric averaging logic
3. proportional scaling
4. decay / reduction models
5. area computation

இது பழந்தமிழ் நில கணக்குகளை நவீன கணித வடிவமாக மாற்றுகிறது.
=========================================================
"""


class NelKanakkuMaatrangal:
    """
    கணக்கதிகாரம் 138–146 அடிப்படையிலான
    நில அளவீட்டு மாற்ற தொகுப்பு.
    """

    # -----------------------------------------------------
    def nel_maatrathil_thirutham(self, value):
        """
    பாடல் 138:
    ஒருகை நிலமாக்கி மறுத்து மறுதுகை
    உடனே மாறி நிலமாம்

        Formula:
            value - (value / 320)

        Returns:
            Fraction
        """
        value = Fraction(value)
        correction = value / 320
        return value - correction

    # -----------------------------------------------------
    def geometrical_land_balance(self, a, b, c):
        """
        பாடல் 139:

        அடியெடு கவடு தாக்கி அதனைஆ றுக்கு யீந்து
        நெடிபடுங் காலில் தாக்கி நின்றன செவ்வி தன்னை
        இடிபடு மட்டில் தாக்க யிருந்ததோ ராலா லுந்தான்
        குடிமிகு குழியென் றோதிக் கூறிட்டார் உலகத் தோரே

        Formula:
            weighted average = (a + b + c) / 3

        Returns:
            Fraction
        """
        return (Fraction(a) + Fraction(b) + Fraction(c)) / 3

    # -----------------------------------------------------
    def decay_land_value(self, value):
        """
        பாடல் 140

        அப்போ அளந்த அடித்தனை முற்றித்துத்
        தட்பாமல் பன்னிரெண்டு தான்கூட்டி-செப்பமுடன்
        பெறஎழுவு இன்பம் பிணிமூப்பு சாவு என்ற
        ஆறுதல் நீத்தே யறி

        Formula:
            value × 0.9

        Returns:
            Fraction
        """
        return Fraction(value) * Fraction(9, 10)

    # -----------------------------------------------------
    def ocean_scale_land(self, area):
        """
        பாடல் 141

        சமுத்திர முறையா இருக்கை அளந்துஆக
        சமுத்திர பாதியங் கறிந்து வைத்தோர்
        உலகை அரையால் மாற ஓதரிய மேனி
        திருவினையால் செவ்வை சமுத்திர மானநிலம் 

        Formula:
            area / 2
        """
        return Fraction(area) / 2

    # -----------------------------------------------------
    def ratio_scaled_land(self, value, ratio):
        """
        பாடல் 142

        இன்னதனை மாவுக்கிறையறிய வென்றுவோர்
        இன்னதனை பூமிக்கிறையென்னில்-மன்னியசீர்
        மாவொடு முந்திரிகை மாகாணி யாக்கொண்டு
        பூவொடு கண்ணார் புகல் 

        Formula:
            value × ratio
        """
        return Fraction(value) * Fraction(ratio)

    # -----------------------------------------------------
    def rectangular_land_area(self, length, breadth):
        """
        பாடல் 143

        அகலவடி நீளவடி தன்னைத்தான் மாறி
        புகலுமொரு மாகாணி யில்பெருக்கி-சிகமறிய
        ஒன்பது பேர்க்கிய ஒருமாவுங் குன்றாமல்
        தன்பதியைக் காக்குந் தடம்.

        Formula:
            length × breadth
        """
        return Fraction(length) * Fraction(breadth)

    # -----------------------------------------------------
    def chained_land_transformation(self, value):
        """
        பாடல் 144

        எண்ணவோ காதம் நூறு இனிநில நூறு மாயச்
        சொன்னது அதனில் மாறிச் சொல்லுக வேலி யென்று
        மன்னியே குலங்கள் உவ வயலது வந்த கையை
        தன்னிலே மாறி மட்டுத் தன்னிலது கழித்துச் சாத்தே

        Formula:
            (value × 10) - (value / 10)
        """
        value = Fraction(value)
        return (value * 10) - (value / 10)

    # -----------------------------------------------------
    def irregular_land_adjustment(self, area):
        """
        பாடல் 145

        பெருங்குழி போலவே பெண்ணங்கே எல்லாம்
        திருந்திரி யித்தனையும் தீர்ந்தால்-பொருந்திய
        மாடங்க ளாக்கியே மாகாணி யாக்கிறை
        கேட்டார் சிறுகுழியாஞ் செப்பு.

        Formula:
            area × 0.95
        """
        return Fraction(area) * Fraction(95, 100)

    # -----------------------------------------------------
    def basic_land_area(self, a, b):
        """
        பாடல் 146
        
        காதத்துக்குக் காதம் நிலங்கருத வேண்டி
        வரிதைபட வேண்டாம் வாணுதல்லே--காதம்
        ரெண்டா யிரத்தில் பெருக்கி......
        திரண்ட நிலம் வேலியெனச் செப்பு.

        Formula:
            a × b
        """
        return Fraction(a) * Fraction(b)


# ==========================================================
# TEST CASES
# ==========================================================

if __name__ == "__main__":

    obj = NelKanakkuMaatrangal()

    print("\n138:", obj.nel_maatrathil_thirutham(100))
    print("139:", obj.geometrical_land_balance(10, 20, 30))
    print("140:", obj.decay_land_value(100))
    print("141:", obj.ocean_scale_land(200))
    print("142:", obj.ratio_scaled_land(100, 0.5))
    print("143:", obj.rectangular_land_area(10, 5))
    print("144:", obj.chained_land_transformation(10))
    print("145:", obj.irregular_land_adjustment(100))
    print("146:", obj.basic_land_area(12, 8))