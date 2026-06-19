"""
உலக அளவு அறிதல் (Ulaga Alavu System)
===================================

கணக்கதிகாரம் நூலில் உள்ள உலக அளவீட்டு முறைகளை அடிப்படையாகக் கொண்டு
மகாமேரு மலையின் உயரம் மற்றும் உலக அமைப்பின் தூர அளவுகள்
இம்மொட்யூலில் தொகுக்கப்பட்டுள்ளன.

இதில் உள்ளவை:
- மகாமேரு உயர அளவீடு
- திசை சார்ந்த உலக தூர அளவுகள்
- பாரம்பரிய புவியியல் கணிதக் குறிப்புகள்

------------------------------------------------------------

This module implements ancient Tamil cosmological measurements
from Kanakkadhigaram.

It includes:
- Mahameru height calculation system
- Directional world distance mapping
- Traditional cosmological reference values
"""

# ==========================================================
# DATA SET
# ==========================================================

WORLD_MEASUREMENTS = {
    "மகாமேரு": {
        "unit": "யோசனை",
        "value": 144000,
        "description": "மகாமேரு மலையின் உயரம்"
    },
    "மூக்குத் தெற்கு": {
        "unit": "காதம்",
        "value": 600,
        "description": "உலக வட்டத்திலிருந்து தெற்குத் தூரம்"
    }
}

# ==========================================================
# CORE FUNCTIONS
# ==========================================================

def get_world_data(name):
    """
    பாடல் 46

    சுளகே ருலகநடுத் தோன்றியமா மேருச்
    சிலைகொளத் தேங்குவிதம் எண்ணில் - இயல்தேரும்
    ஆறாறும் ஆயிரமி யோசனைமூக் குத்தெற்கு
    நூறாது காதம் நுவல்.

    """

    if name not in WORLD_MEASUREMENTS:
        raise ValueError(f"Unknown measurement: {name}")

    return WORLD_MEASUREMENTS[name]

def get_world_value(name):
    return get_world_data(name)["value"]

def list_world_items():
    return list(WORLD_MEASUREMENTS.keys())

# ==========================================================
# TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("WORLD ITEMS:")
    print(list_world_items())

    print("\nSAMPLE OUTPUT:\n")

    for name in list_world_items():
        data = get_world_data(name)

        print(f"{name}")
        print(f"  → Value : {data['value']} {data['unit']}")
        print(f"  → Description : {data['description']}")
        print("-" * 40)