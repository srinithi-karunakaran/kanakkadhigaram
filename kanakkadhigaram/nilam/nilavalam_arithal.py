"""
நிலவளம் அறிதல் (Nilavalam Soil Intelligence System)
====================================================

Ancient Tamil agricultural classification system from Kanakkadhigaram (பாடல் 85).

This module provides:
- Soil → Plant mapping
- Plant → Soil recommendation
- Soil fertility classification system
"""

# ==========================================================
# SOIL CLASSIFICATION SYSTEM (from verse 85)
# ==========================================================

SOIL_SYSTEM = {
    "உத்தமநிலம்": [
        "குவளை", "சடை", "கரந்தை", "காவேடு",
        "காவேளை", "பவளக்கொடி", "புல்", "சேற்றுப்பயிர்"
    ],

    "மத்திமநிலம்": [
        "செருப்பை", "துராய்", "கண்டங்கத்திரி",
        "வேல்", "அறுகு", "சாமை", "கேழ்வரகு"
    ],

    "அதமநிலம்": [
        "பொடுதலை", "பொரி", "விரை", "துடப்பம்", "உவர்"
    ]
}

# ==========================================================
# REVERSE INDEX (Plant → Soil)
# ==========================================================

PLANT_TO_SOIL = {}

for soil, plants in SOIL_SYSTEM.items():
    for plant in plants:
        PLANT_TO_SOIL[plant] = soil


# ==========================================================
# CORE FUNCTIONS
# ==========================================================

def get_soil_for_plant(plant_name):
    """
    பாடல் 85:
    உற்றசீர் பூமி அதனில் ஒளிவளம்
    கொற்றவேற் கண்ணாய் குவளையேழும் - மற்றை
    இடைநிலத்து வேல்துராய் என்றிவைகள் ஆகும்
    கடைநிலத்து வெண்மைஉவர் காண்.

    Parameters
    ----------
    plant_name : str
        பயிர் பெயர்

    Returns
    -------
    str
        நில வகை (உத்தம / மத்திம / அதம)
    """
    return PLANT_TO_SOIL.get(plant_name, "தெரியாத பயிர்")


def get_plants_for_soil(soil_type):
    """
    கொடுக்கப்பட்ட நிலத்துக்கு ஏற்ற பயிர்கள்

    Parameters
    ----------
    soil_type : str
        நில வகை பெயர்

    Returns
    -------
    list
        பயிர்களின் பட்டியல்
    """
    return SOIL_SYSTEM.get(soil_type, [])


# ==========================================================
# RECOMMENDER 
# ==========================================================

def recommend_soil(plant_list):
    """
    பல பயிர்களுக்கு பொதுவான சிறந்த நிலம்

    Parameters
    ----------
    plant_list : list
        பயிர் பெயர்கள்

    Returns
    -------
    str
        பரிந்துரைக்கப்படும் நில வகை
    """

    score = {"உத்தமநிலம்": 0, "மத்திமநிலம்": 0, "அதமநிலம்": 0}

    for plant in plant_list:
        soil = PLANT_TO_SOIL.get(plant)
        if soil:
            score[soil] += 1

    return max(score, key=score.get)


# ==========================================================
# UTILITIES
# ==========================================================

def list_soils():
    return list(SOIL_SYSTEM.keys())

def list_all_plants():
    return list(PLANT_TO_SOIL.keys())


# ==========================================================
# TEST BLOCK
# ==========================================================

if __name__ == "__main__":

    print("=== PLANT → SOIL ===")
    print("குவளை:", get_soil_for_plant("குவளை"))
    print("சாமை:", get_soil_for_plant("சாமை"))

    print("\n=== SOIL → PLANTS ===")
    print("உத்தமநிலம்:", get_plants_for_soil("உத்தமநிலம்"))

    print("\n=== RECOMMENDER ===")
    print(recommend_soil(["குவளை", "சாமை", "அறுகு"]))