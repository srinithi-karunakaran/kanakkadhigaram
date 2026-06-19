"""
கணக்கதிகாரம் – பொருள் அளவியல் செயலாக்க நூலகம்
=============================================

இந்த module பழமையான தமிழ் கணக்கதிகார பாடல்களில் வரும்
மாத்து, பொன், வெள்ளி, கழஞ்சு போன்ற அளவீட்டு கணக்குகளை
நேரடியாக செயல்படுத்தும் ஒரு கணக்கியல் இயந்திரமாகும்.

அம்சங்கள்:
- விகித (ratio) மாற்றங்கள்
- பெருக்கல் / வகுத்தல் அடிப்படையிலான மாற்றங்கள்
- சேர்த்தல் மற்றும் கழித்தல் செயல்முறைகள்
- எடை அடிப்படையிலான பகிர்வு
- கலப்பு உலோக (பொன்–வெள்ளி) கணக்கீடுகள்

"""

from fractions import Fraction

# =========================================================
# proportional_transform
# =========================================================

def proportional_transform(maathu: int) -> dict:
    """
    பாடல் 183:
    ஒக்கும் பொன்னாக ஒன்றிரண்டு தாழ்ந்தவற்றின்
    மிக்க மதியால் விளம்பென்றால் — அக்கணக்குச்
    சொன்னதனை மாற்றாகத் தொகையாக்கிச் செவ்வைக்கே
    இன்னதனைப் பொன்னென் றியம்பு.

    Parameters
    ----------

    maathu : int
        Input maathu value

    Returns
    -------
    dict
        Stepwise transformed values
    """

    step1 = maathu * 2
    step2 = step1 / 8

    return {
        "input": maathu,
        "step_1": step1,
        "step_2": step2
    }


# =========================================================
# relation_structure
# =========================================================

def relation_structure() -> dict:
    """
    பாடல் (184):
    தின்பொனுக்குத் தன்பொன்னைத் தந்திடினும் சேயிழையாப் 
    தன்பொனுக்குத் தின்பொன்னைத் தாவெனினும்- நண்புள்ள
    முன்மாத்தைப் பின்பொனால் மாறிமுறை வந்ததொகை
    பின்மாத்துக் கீய்ந்தே யியம்பு.

    Parameters
    ----------
    verse : str

    Returns
    -------
    dict
        Structural operations only
    """

    return {
        "operations": [
            "swap_relation",
            "reverse_mapping",
            "ratio_interchange",
            "division_structure"
        ]
    }


# =========================================================
# cumulative_sum_transform
# =========================================================

def cumulative_sum_transform() -> dict:
    """
    பாடல் (185):
    மாத்து தோறும் தான்சிறிது பொன்னுருக்கி 
    மிக்க வகையால் விளம்பென்றால் - அக்கணமே
    மாத்துத்தோ றும்பெருக்கி மாத்துத் தொகைக்கீய
    மாத்துதோ றும்பொன் வரும்.

    Parameters
    ----------
    verse : str

    Returns
    -------
    dict
        Computed accumulation result
    """

    values = [10, 9, 8, 7, 6]

    total = sum(values)
    scaled = total * 1000
    result = scaled / 40

    return {
        "values": values,
        "sum": total,
        "scaled": scaled,
        "result": result
    }


# =========================================================
# product_scale_transform
# =========================================================

def product_scale_transform( gold: int, silver: int) -> dict:
    """
    பாடல் 186:
    (ய)பத்து மாத்தில் சிலபொன்னில் பாய்ந்த வெள்ளி நூறாகி
    ஒத்த மாத்துட னேத்தியதா ........... ........... ...........
    முன்மாத்தி லாறு ........... முடியாத மாத்தா னாலும்
    கன்புத்த யீய நின்ற ........... ...பொன் னாகுமே

    Parameters
    ----------
    verse : str
    gold : int
    silver : int

    Returns
    -------
    dict
        Product-based transformation result
    """

    step1 = gold * silver
    step2 = step1 / 10

    return {
        "gold": gold,
        "silver": silver,
        "product": step1,
        "scaled": step2
    }


# =========================================================
# add_remove_balance
# =========================================================

def add_remove_balance(value: int) -> dict:
    """
    பாடல் 187:
    அன்னமென் நடையினாளே அருந்ததி அனைய மாதே
    பொன்னுடன் புகுந்த வெள்ளி புக்கது தோன்று வண்ணஞ்
    சொன்னபொன் மாத்தால் மாறிச் சுருக்கிய மாத்துக் கீய
    பின்னையுமுன் சொன்னண்ணம் நீக்கிப் பிறந்தது வெள்ளி யாமே

    Parameters
    ----------
    verse : str
    value : int

    Returns
    -------
    dict
        Balanced transformation output
    """

    added = value * Fraction(1, 2)
    removed = value * Fraction(1, 4)

    return {
        "input": value,
        "added": added,
        "removed": removed,
        "result": value + added - removed
    }


# =========================================================
# weighted_square_transform
# =========================================================

def weighted_square_transform() -> dict:
    """
    பாடல் 188:
    மாத்திற் கழஞ்சுபொன்னில் மாறும் விலையுரைத்து
    மாத்திற் கழஞ்சுபின்னே மாற்றென்ன--யேற்றவிலை
    முன்கழஞ்சுக் கீந்து நடுமாற் றுடன்பெருக்கிப்
    பின்கழஞ்சுக் கீந்து பிழை.

    Parameters
    ----------
    verse : str

    Returns
    -------
    dict
        Squared weighted transformation result
    """

    values = [10, 9, 8, 7, 6]

    squares = [v * v for v in values]
    total = sum(squares)
    result = total / 40

    return {
        "values": values,
        "squares": squares,
        "total": total,
        "result": result
    }


# =========================================================
# average_like_merge
# =========================================================

def average_like_merge( values: list) -> dict:
    """
    பாடல் 189:
    மாத்துப் பொன்னதனைக் கூட்டி யுருக்கிவைத்தே
    மாத்தா மென்று வினவினால் — மாத்தை
    மற்றந்த பொன்னால் மாறியவன் சொன்ன
    பொற்றொகைக் கீய்ந்து புகல்.

    Parameters
    ----------
    verse : str
    values : list[int]

    Returns
    -------
    dict
        Reduced merged value
    """

    total = sum(values)
    reduced = total / len(values)

    return {
        "values": values,
        "sum": total,
        "reduced": reduced
    }


# =========================================================
# normalized_square_merge
# =========================================================

def normalized_square_merge(values: list) -> dict:
    """
    பாடல் 190:
    பலமாத்துப் பொன்னதனைக் கூட்டி யுருக்கிச்
    சிலமான எத்தனையமாற் றென்று வினவினால்
    மாத்தைப் பொன்னால் அந்தவன் சொன்ன
    செம்மையிடை சேர்ந்திதனைச் செப்பு.

    Parameters
    ----------
    verse : str
    values : list[int]

    Returns
    -------
    dict
        Normalized weighted result
    """

    weighted = [v * v for v in values]
    result = sum(weighted) / len(values)

    return {
        "values": values,
        "weighted": weighted,
        "result": result
    }


# =========================================================
# difference_extraction
# =========================================================

def difference_extraction( base: int, final: int) -> dict:
    """
    பாடல் 191:
    எழுமாத்துப் பொன்னதனில் இட்டுருக்கக் கண்ட
    விழுமாத்தின் வெள்ளி வினவின்-- முழுமாத்தை
    மற்றந்தப் பொன்னாலே மாறி யவன்சொன்ன
    பொற்றொகைக் கீய்ந்து புகல்.

    Parameters
    ----------
    verse : str
    base : int
    final : int

    Returns
    -------
    dict
        Difference output
    """

    return {
        "base": base,
        "final": final,
        "difference": final - base
    }


# =========================================================
# scale_conversion
# =========================================================

def scale_conversion(value: int) -> dict:
    """
    பாடல் 192:
    மாத்தறியா தின்னதனைப் பொன்னுக்கு வானுதலாய்!
    தோற்றிய செம்பொன் சொன்னதொகை - மாத்துரையீர்!
    வன்பொன்னின் மாற்றாலே மாறி யவன்நிலையெ
    முன்பொன்னாய் வித்து மொழி.

    Parameters
    ----------
    verse : str
    value : int

    Returns
    -------
    dict
        Scaled output
    """

    return {
        "input": value,
        "scaled": value * Fraction(8, 10)
    }


# =========================================================
# additive_adjustment
# =========================================================

def additive_adjustment(value: int) -> dict:
    """
    பாடல் 193:
    அந்தமு மாதியு மேரினமே யாகில்
    சந்தனையுந் தாக்கியபின் தானாக - முந்தவே
    பெற்ற பயனைப் பிழையாம லீந்ததுவே
    பொற்றொடியாய் நீநிறுக்கும் பொன். 
    
    Parameters
    ----------
    verse : str
    value : int

    Returns
    -------
    dict
        Adjusted value
    """

    return {
        "input": value,
        "result": value + 3
    }


# =========================================================
# weighted_distribution
# =========================================================

def weighted_distribution( total: int = 1000) -> dict:
    """
    பாடல் 194:
    மாகாணி பத்துமா ஆகுமொரு மஞ்சாடி
    ஆமாகில் முக்காணிக் காறுமா--ஆமதனில்
    குன்றிக் கரைமா பிளவுக்கோர்காணியாம்
    நின்ற வரைக்காணி நேர்

    Parameters
    ----------
    verse : str
    total : int

    Returns
    -------
    dict
        Distribution mapping
    """

    weights = [10, 9, 8, 7, 6]
    total_w = sum(weights)

    return {
        "distribution": {
            w: Fraction(w * total, total_w)
            for w in weights
        }
    }



# =========================================================
# TEST CASES
# =========================================================

if __name__ == "__main__":

    sample_verse = "கணக்கதிகாரம் பாடல்"

    print("Proportional:", proportional_transform(sample_verse, 10))
    print("Relation:", relation_structure(sample_verse))
    print("Cumulative:", cumulative_sum_transform(sample_verse))
    print("Gold-Silver:", product_scale_transform(sample_verse, 10, 5))
    print("Balance:", add_remove_balance(sample_verse, 10))
    print("Square:", weighted_square_transform(sample_verse))
    print("Merge:", average_like_merge(sample_verse, [10, 9, 8]))
    print("Normalize:", normalized_square_merge(sample_verse, [10, 9, 8]))
    print("Difference:", difference_extraction(sample_verse, 10, 12))
    print("Scale:", scale_conversion(sample_verse, 10))
    print("Add:", additive_adjustment(sample_verse, 10))
    print("Distribution:", weighted_distribution(sample_verse))
 