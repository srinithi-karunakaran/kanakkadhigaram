"""
செவிடு எண்ணிக்கை அளவை அறிதல் (Sevidu En Alavai System)
=====================================================

Ancient Tamil quantity system from Kanakkadhigaram (பாடல்கள் 57-58).

This module includes:
- One Sevidu item mapping system
- Conversion between Sevidu and item counts
"""

# ==========================================================
# DATA
# ==========================================================

SEVIDU_COUNTS = {
    "கடுகு": 23400,
    "எள்ளு": 2880,
    "நெல்": 360,
    "அரிசி": 450,
    "பயறு": 360,
    "காணம்": 360,
    "மிளகு": 320,
    "துவரை": 180
}

# ==========================================================
# CORE FUNCTIONS
# ==========================================================

def get_item_value(item):
    """
    பாடல் 57

    ஐயிரு பத்துமு வாயிரத்து நாற்பத்தே
    ளெய்திரண்டா யிரத்தொண்ணூற் றோரொன்பது
    முன்னூற் றுறுபதுநெல் முழுவரிசி செவிடாக
    நாநூற்றோ டைம்பதே நாட்டு.

    பாடல் 58
    முழுப்பயறு முன்னூற் றறுபதுகொள் முன்னூறு
    நளப்பமுட னேமிளகு நாற்பத்தெட - டளப்பமுடன்
    நூற்றெண்ப தைவாறு நுண்ணிமையா லெண்ணாத
    ஈற்றமுள்ள திப்படி எண்.

    Parameters
    ----------
    item : str
        பொருளின் பெயர்

    Returns
    -------
    int
        ஒரு செவிடில் உள்ள எண்ணிக்கை
    """

    if item not in SEVIDU_COUNTS:
        raise ValueError(f"Unknown item: {item}")
    return SEVIDU_COUNTS[item]


def sevidu_to_item(sevidu, item):
    """Convert Sevidu → item count"""
    return sevidu * get_item_value(item)


def item_to_sevidu(count, item):
    """Convert item count → Sevidu"""
    return count / get_item_value(item)

# ==========================================================
# UTILITIES
# ==========================================================

def list_sevidu_items():
    return list(SEVIDU_COUNTS.keys())


# ==========================================================
# TEST BLOCK (PYPI SAFE)
# ==========================================================

if __name__ == "__main__":

    # Test 1: list items
    items = list_sevidu_items()

    # Test 2: Sevidu → item
    test_1 = sevidu_to_item(1, "நெல்")
    test_2 = sevidu_to_item(2, "மிளகு")

    # Test 3: item → Sevidu
    test_3 = item_to_sevidu(720, "நெல்")
    test_4 = item_to_sevidu(23400, "கடுகு")

    # Print raw outputs (for verification only)
    print("ITEM LIST:", items)
    print("1 Sevidu → நெல்:", test_1)
    print("2 Sevidu → மிளகு:", test_2)
    print("720 நெல் → Sevidu:", test_3)
    print("23400 கடுகு → Sevidu:", test_4)