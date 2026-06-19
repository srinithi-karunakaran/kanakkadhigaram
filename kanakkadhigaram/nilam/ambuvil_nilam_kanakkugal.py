"""
கணக்கதிகாரம் – அம்பு, வில் மற்றும் பல வடிவ நில அளவியல் கணக்குகள்

இந்த module, தமிழின் பழமையான கணக்கதிகாரம் நூலிலிருந்து
எடுக்கப்பட்ட நில அளவியல் முறைகளை Python வடிவில் வழங்குகிறது.

இதில் உள்ள கணக்குகள்:
- அம்பு/வில் வடிவ நிலங்கள்
- ஐங்கோணம் மற்றும் பல்கோணம் approximation
- கலப்பு வடிவ நிலங்கள்
- சராசரி அடிப்படையிலான பழமையான அளவியல் கணக்குகள்

இவை அனைத்தும் பழமையான தமிழ் கணித முறைகளை
நவீன கணித வடிவத்துடன் இணைத்து உருவாக்கப்பட்டவை.
"""

def ampu_vil_nilam(length: float, breadth: float) -> float:
    """
    பாடல் (168)
    அப்புத் தலையின் அளவின் அரைதன்னைச்
    செப்பும் நீளத்தால் தெரி.

    Parameters:
        length (float): நீளம்
        breadth (float): அகலம்

    Returns:
        float: அம்பு வடிவ நிலப் பரப்பு
    """
    return (length * breadth) / 2

def ainkona_nilam(sides: list) -> float:
    """
    பாடல் (169)
    சதிரத்தின் மேல்வைத்த கையனைத்துங் கூட்டி
    முத்துகை யாக முன்னிறுத்திப் - பிதிர்ந்து
    கையிரண்டு கூறாய்ப் பிளந்து ஏந்திழையாய்
    ஓரிரண்டில் மாறி யுரை.

    Parameters:
        sides (list): பக்க அளவுகள்

    Returns:
        float: நில அளவு
    """
    avg = sum(sides) / len(sides)
    return avg * avg

def pal_mugam_nilam(sides: list) -> float:
    """
    பாடல் (170)
    ஐங்கோண மறுகோணம் என்றுவந்த நிலமெல்லாம்
    சூடி வளர்ந்து கூடினதுகை - நாலு
    கூறிட்டு ஒருகூறின் பயதன் னோடே
    தன்னை மாறிகுழி சொல்

    Parameters:
        sides (list): பக்கங்கள்

    Returns:
        float: நில அளவு
    """
    return sum(sides) * (sum(sides) / len(sides)) / 4

def kalappu_nilam(a: float, b: float, c: float) -> float:
    """
    பாடல் (171)
    வானமே அஞ்சு கோணம் வரும்பெருகும் குழிய வத்துள்
    நீளடி மத்த னந்தான் நடுகையே குறுங்கை நல்கய
    ஈளமி லிசைந்து நீள கைநெடுங் கையிற் தாக்கி
    மீன்குழி யெனவி ளங்கி ..... தாக்க கூட்டே

    Parameters:
        a (float): முதல் அளவு
        b (float): இரண்டாம் அளவு
        c (float): மூன்றாம் அளவு

    Returns:
        float: கலப்பு நில அளவு
    """
    return (a * b + b * c) / 2

def vil_nilam(length: float, breadth: float) -> float:
    """
    பாடல் (172)
    அம்புடன் நாணை அரையாக்கி ஆங்கதனை
    அம்புடனே மாறி அறிந்தக்கால் - கொம்பனையாய்
    வில்லாகி நின்ற நிலங்கள் குழிபிழைத்து
    நில்லா தெனவே நினை.

    Parameters:
        length (float): நீளம்
        breadth (float): அகலம்

    Returns:
        float: நில அளவு
    """
    return (length * breadth) / 2

def vil_ambu_nilam(parts: list) -> float:
    """
    பாடல் (173)
    அம்பினால் மூன்று தாக்கும் அளந்துமுப் பிளவு செய்து
    நம்புரை ணளவு மூன்றை நாடிமுப் பிளவு செய்து
    பின்புடன் துகையி ரண்டும் ஏற்றியே கூட்டிச் சொல்லத்
    தும்புசேர் குழினாலே தோன்றிலுங் குழிகள் தானே.

    Parameters:
        parts (list): அளவுகள்

    Returns:
        float: நில அளவு
    """
    avg = sum(parts) / len(parts)
    return avg * avg

def ambu_nan_nilam(arrow: float, string: float) -> float:
    """
    பாடல் (174)
    அம்பையும் நாணையும் அமர்பாதி யாக்கி
    அம்புடனே குழிசொல்வது தான்.

    Parameters:
        arrow (float): அம்பு அளவு
        string (float): நாண் அளவு

    Returns:
        float: நில அளவு
    """
    return (arrow * string) / 2

if __name__ == "__main__":

    print("168:", ampu_vil_nilam(10, 8))
    print("169:", ainkona_nilam([4, 5, 6, 7, 8]))
    print("170:", pal_mugam_nilam([3, 4, 5, 6]))
    print("171:", kalappu_nilam(4, 5, 6))
    print("172:", vil_nilam(10, 8))
    print("173:", vil_ambu_nilam([5, 6, 7]))
    print("174:", ambu_nan_nilam(12, 15))