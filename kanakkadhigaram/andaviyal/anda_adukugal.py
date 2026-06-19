"""
சூரியர்–சந்திரர் மண்டல அமைப்பு (Cosmic Layer System)
====================================================

கணக்கதிகாரம் பாடல்கள் 49-50 அடிப்படையில்
பிரபஞ்ச மண்டல அடுக்குகள் மற்றும் தூர அமைப்பு.

This module models ancient Tamil cosmological layers
and their relative distance mapping concepts from Kanakkadhigaram.
"""

# ==========================================================
# DATA SET
# ==========================================================

COSMIC_LAYERS = [
    "பூமி",
    "மேக மண்டலம்",
    "ஆதித்த மண்டலம்",
    "செவ்வாய் மண்டலம்",
    "புதன் மண்டலம்",
    "பிரகஸ்பதி மண்டலம்",
    "சுக்கிர மண்டலம்",
    "சனி மண்டலம்",
    "இராகு மண்டலம்",
    "கேது மண்டலம்",
    "தெய்வ லோகம்",
    "விஷ்ணு லோகம்"
]

# distance per layer step (verse-based approximation)
LAYER_DISTANCE = 24000  # யோசனை


# ==========================================================
# CORE FUNCTIONS
# ==========================================================

def list_layers():
    """
    பாடல் 49
    மண்ணளவை மாற்றியது வண்கதிர்கள் வானளவாம்
    எண்ணளவாய்க் கொண்டார் இயம்பியே — எண்ணின்
    பெருகவே ஏழ்கடலின் மற்றவையொன் றொன்றின்
    பெருக்கமே யேழ்கடலின் பீடு.

    பாடல் 50
    காத நான்கும் யோசனை ஆகவே எவர்க்குத் தானும்
    ஆதித்த மண்டலம் நான்கு ஆயிரம் யோசினை ஆகும்
    மாதவா மாற வேளை வாரண மற்று மற்றும்
    ஓதவே தனனம் ..... ஒன்றைப் பகரு வாயே.
    """
    return COSMIC_LAYERS


def get_layer_index(layer):
    """
    ஒரு மண்டலத்தின் index பெறுதல்
    """
    if layer not in COSMIC_LAYERS:
        raise ValueError(f"தெரியாத மண்டலம்: {layer}")

    return COSMIC_LAYERS.index(layer)


def get_layer_distance_step():
    """
    ஒரு அடுக்கு இடைவெளி (யோசனை)
    """
    return LAYER_DISTANCE


def distance_from_earth(layer):
    """
    பூமியிலிருந்து குறிப்பிட்ட மண்டலத்திற்கு தூரம்

    Formula:
        index × layer_distance
    """
    index = get_layer_index(layer)
    return index * LAYER_DISTANCE


def get_cosmic_map():
    """
    முழு மண்டல அமைப்பு + தூரம் mapping
    """
    return {
        layer: i * LAYER_DISTANCE
        for i, layer in enumerate(COSMIC_LAYERS)
    }


# ==========================================================
# OPTIONAL UTILITIES
# ==========================================================

def is_valid_layer(layer):
    """Check if layer exists"""
    return layer in COSMIC_LAYERS


# ==========================================================
# TEST BLOCK 
# ==========================================================

if __name__ == "__main__":

    print("=== COSMIC LAYERS ===")
    print(list_layers())

    print("\n=== DISTANCES ===")
    for layer in COSMIC_LAYERS:
        print(layer, "->", distance_from_earth(layer), "யோசனை")