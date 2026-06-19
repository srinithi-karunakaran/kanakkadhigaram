"""
கணக்கதிகாரம் (Kanakkadhigaram) – வட்டம் மற்றும் விட்டம் சார்ந்த கணக்குகள்

இந்த module-ல் உள்ள கணக்குகள் தமிழின் பழமையான
கணக்கதிகாரம் நூலிலிருந்து பெறப்பட்டவை.

இதில்:
- விட்டத்திலிருந்து வட்டப் பரப்பு கணக்கிடுதல்
- சுற்றளவிலிருந்து விட்டம் கண்டறிதல்
- மோதிர வடிவ நிலம் கணக்குகள்
- வட்ட மாற்றக் கணித சூத்திரங்கள்


"""

def vattam_purappu_kanakku(vittam: float) -> float:
    """
    பாடல் (161)
    விட்டம் இரட்டித்து நால்மாவில் வாட்டிய
    தெட்ட லேட்ட வட்டத்தளவா குங்கு.

    Parameters:
        vittam (float): வட்டத்தின் விட்டம்

    Returns:
        float: வட்டத்தின் பரப்பு (குழி அளவு)
    """
    return (vittam * vittam) / 8

def vattam_irattipu_mattram(vittam: float) -> float:
    """
    பாடல் (162)

    மூன்றொரு நாலு மாவை விட்டத்தால் பெருக்க
    மூன்றில் தோன்றிய கடை... கோல்கள் சுற்றத்து வட்ட மாமே
    ஆற்றவச் சுற்றந் தன்னை ஆறுமா காணிக் கீய
    என்றவத் துகைகள் தானே விட்டமென் றெண்ணினாரே

    Parameters:
        vittam (float): விட்டம்

    Returns:
        float: வட்ட பரப்பு
    """
    return (2 * vittam) ** 2 / 8

import math

def sutralaavu_to_vattam(sutralaavu: float) -> float:
    """
    பாடல் (163)

    ஆங்குசெய்யும் வட்டத்தை ஆறுமாக் கானிதனில்
    பாங்குடனே மாறும் பயன்விட்டம் — நீங்கி
    முறுக்கிவிடு வட்டத்தை முன்னோடுப நாலில்
    பெருக்கிவிட வட்டமெனப் பேசு.

    Parameters:
        sutralaavu (float): சுற்றளவு

    Returns:
        float: வட்டப் பரப்பு
    """
    vittam = sutralaavu / math.pi
    return (vittam * vittam) / 8

def mothiram_vattam_nilam(ul_vattam: float, veli_vattam: float) -> float:
    """
    பாடல் (164)
    மோதிரத்தைச் சுழன்று மூன்றாறு பங்காக்கி
    அதில்நடு ஒருஅளவு அளந்து - இதுரெண்டை
    ஒக்கவே தாக்குக்கு மாற ஒண்ணுதலாய்
    தக்கதே ஆகும் தாம்.

    Parameters:
        ul_vattam (float): உள்ள விட்டம்
        veli_vattam (float): வெளி விட்டம்

    Returns:
        float: மோதிர வடிவ நிலம்
    """
    return (veli_vattam * veli_vattam - ul_vattam * ul_vattam) / 8


def pilavu_vattam(parts: list) -> float:
    """
    பாடல் (165)
    மோதிர வட்டத் தன்னை நெடுக்குமுன் றளவந்து
    ...... ...... ...... ...... ...மூன் றத்தொன்றாக்கியே
    இதனை யளந்தாப் போலே அளந்துப் பிளவு செய்து
    ஏதலி ரண்டு மாற எளிவருங் குழிகள் தானே.

    Parameters:
        parts (list): பகுதி விட்டங்கள்

    Returns:
        float: மொத்த வட்ட அளவு
    """
    return sum([(p * p) / 8 for p in parts])

def vattam_ilirundhu_vittam(purappu: float) -> float:
    """
    பாடல் (166)
    அம்பாகி நின்ற நிலங்கள் அளப்பதற்கு
    செம்பாதி நீளம் செப்பியதால் - அம்பான
    தன்னாலே மாறத் தவள நகைமடவாய்
    என்னாளும் குன்றா திரு.

    Parameters:
        purappu (float): வட்டப் பரப்பு

    Returns:
        float: விட்டம்
    """
    return (purappu * 8) ** 0.5

def ethir_vattam_mattram(purappu: float) -> float:
    """
    பாடல் (167)
    அப்புத் தலையை அரைநீளத் தால்மாறி
    செப்புக் குழியிழைத் தேன்.

    Parameters:
        purappu (float): வட்டப் பரப்பு

    Returns:
        float: விட்டம்
    """
    return (purappu * 8) ** 0.5

if __name__ == "__main__":

    print("161:", vattam_purappu_kanakku(10))
    print("162:", vattam_irattipu_mattram(10))
    print("163:", sutralaavu_to_vattam(40))
    print("164:", mothiram_vattam_nilam(5, 10))
    print("165:", pilavu_vattam([10, 12, 8]))
    print("166:", vattam_ilirundhu_vittam(50))
    print("167:", ethir_vattam_mattram(50))