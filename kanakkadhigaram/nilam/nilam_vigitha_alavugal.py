"""
=========================================================
நாற்சதுர நில விகித கணக்குகள் (பாடல் 112-18)
=========================================================

இது Kanakkadhigaram நூலிலிருந்து எடுக்கப்பட்ட
பழந்தமிழ் நில அளவீட்டு மற்றும் விகித கணக்குகள் தொகுப்பு.

முக்கிய கருத்துகள்:

1. பங்கு (Fraction) அடிப்படையிலான நில மாற்றம்
2. விகித (Ratio) அடிப்படையிலான அளவீடு
3. குறுக்கு பெருக்கல் (Cross multiplication)
4. எதிர் விகித மாற்றம் (Inverse scaling)
5. தொடர்ச்சியான விகித கணக்குகள் (Chained ratios)

பொதுச் சூத்திரங்கள்:

- பங்கு மாற்றம்:
    value × (fraction)

- விகித மாற்றம்:
    value × (a / b)

- குறுக்கு பெருக்கல்:
    y = (x2 × y1) / x1
"""

from fractions import Fraction


class NilamVigithaAlavugal:
    """
    பாடல் 112–118 : பழந்தமிழ் நில விகித கணக்குகள்

    This class explains land measurement conversions,
    fractional scaling, and ratio-based calculations.
    """

    @staticmethod
    def fractional_land_conversion(base_value, fraction):
        """
         பாடல் 112
        அளந்தகை நான்கும் அளவறிந்து கூட்டிப்
        பிளந்து பெரியதனால் பெருக்கி — அளந்ததனை
        மட்டினால் தாக்கி மாகாணி யிற்கழிக்க
        விட்டோர் விளங்குங் குழி

        பாடல் 113
        அடிக்கடியாங் கோலதனை ஆனகை தாக்குமாகில்
        அப்படியே ஆங்கதனை மாறி — அடிக்கிலக்கு
        மேலிலக்க மீந்தவனை வேண்டிமுன் சொன்னகுழி
        கோலி(ல்)வைக்கத் தோன்றுங் குழி.

        Description:
        Fraction-based land conversion.

        Parameters:
            base_value (float): Base land value
            fraction (str | Fraction): Fraction value (e.g. "1/4")

        Returns:
            float | Fraction: Converted value
        """
        return base_value * Fraction(fraction)

    @staticmethod
    def ratio_conversion(base_value, a, b):
        """
        பாடல் 114
        கோலடி மாறி குழிதனைப் பெருக்கி
        கோலடி அறியா குழிதனக் கீழந்து
        வாரிய கோலை வர்க்கஞ் செய்ய
        சீரிய கோலும் சிறந்த தாமே.
        
        பாடல் 115
        அளந்தகோல் எத்தனை என்றால் கோல் வருக்கத்தால்
        குழிமாறி சொல்வறியா குழிதனக் கீய்ந்து
        வாரிய பலத்தை வருத்தமுஞ் செய்ய
        சீரிய கோலும் சிறந்துடன் தோன்றி.

        Description:
        Ratio-based conversion between two scales.

        Parameters:
            base_value (float): Base value
            a (float): New scale value
            b (float): Old scale value

        Returns:
            float | Fraction: Scaled value
        """
        return base_value * Fraction(a, b)

    @staticmethod
    def cross_multiplication(x1, y1, x2):
        """
        பாடல் 116
        முந்துகோ லடிபைக் கையுந் தாக்குடன் மொழிந்து வைத்துப்
        பிந்தவான குழியில் முந்துங் குழியினைக் கழித்து அதனை
        முந்தவான கையுறத் தாக்கில் மொழிந்தனச் சரியே யாகப்
        பிந்தவோர் தாக்கு ஏந்தி இருகைகோ லடியின் பேரே.

        Description:
        Cross multiplication method for proportional values.

        Parameters:
            x1 (float): First known value
            y1 (float): First known result
            x2 (float): New input value

        Returns:
            Fraction: Computed proportional result
        """
        return Fraction(x2 * y1, x1)

    @staticmethod
    def chained_ratio(base, ratios):
        """
        பாடல் 117
        எட்டிய கோலால் இருபதி னாயிரமாம்
        எட்டியொரு கோலில் தான் அளக்க—திட்டமாம்
        நாற்பதி கோலுக்கு நாநூறு குழிக்குத்
        தேற்ப விசைப்பதே இன்று.

        Description:
        Sequential multiplication of multiple ratios.

        Parameters:
            base (float): Base value
            ratios (list): List of ratio values

        Returns:
            Fraction: Final computed value
        """
        result = Fraction(base)
        for r in ratios:
            result *= Fraction(r)
        return result

    @staticmethod
    def inverse_ratio(base_value, a, b):
        """
        பாடல் 118
        கோலை கோலால் தான்தாக்கி கோல தன்னை மட்டோடும்
         ...... கருதி தாக்க வல்லீராய்
        எல்லாந் துள்ள கணக்கெல்லாம் நல்ல கமல மலர்முகத்துச்
        சேலிற் பொழியும் கன்மடவீர் தெளியுங் குழிகள் திண்ணெனவே.

        Description:
        Inverse ratio scaling method.

        Parameters:
            base_value (float): Base value
            a (float): Numerator scale
            b (float): Denominator scale

        Returns:
            float | Fraction: Inverse scaled value
        """
        return base_value * Fraction(b, a)


if __name__ == "__main__":

    from kanakkadhigaram.nilam.nilam_vigitha_alavugal import NilamVigithaAlavugal as NV

    print("Fractional Conversion:", NV.fractional_land_conversion(100, "1/4"))

    print("Ratio Conversion:", NV.ratio_conversion(100, 3, 4))

    print("Cross Multiplication:", NV.cross_multiplication(24, 100, 16))

    print("Chained Ratio:", NV.chained_ratio(10, ["1/4", "1/2", "3/5"]))

    print("Inverse Ratio:", NV.inverse_ratio(100, 3, 4))