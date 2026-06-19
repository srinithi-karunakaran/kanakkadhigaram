from kanakkadhigaram.andaviyal import *

import pytest


# =========================================================
# NAKSHATRA LOOKUP TESTS
# =========================================================

def test_nakshatra_to_nazhi():
    result = nakshatra_to_nazhi("அசுபதி")

    assert result["nakshatra"] == "அசுபதி"
    assert result["symbol"] == "குதிரை தலை"
    assert result["nazhi"] == 2


def test_rohini_nazhi():
    result = nakshatra_to_nazhi("ரோகிணி")

    assert result["nazhi"] == 12


# =========================================================
# TOTAL NIGHT TIME TESTS
# =========================================================

def test_total_night_nazhi():
    total = total_night_nazhi(
        ["அசுபதி", "பரணி", "கார்த்திகை"]
    )

    assert total == 13


def test_total_night_nazhi_single():
    total = total_night_nazhi(["சுவாதி"])

    assert total == 1


def test_total_night_nazhi_empty():
    assert total_night_nazhi([]) == 0


# =========================================================
# SYMBOL LOOKUP TESTS
# =========================================================

def test_get_symbol():
    assert get_symbol("சதயம்") == "தவிட்டுச் சதயம்"


def test_get_symbol_unknown():
    assert get_symbol("XYZ") is None


# =========================================================
# LIST TESTS
# =========================================================

def test_list_nakshatras():
    stars = list_nakshatras()

    assert "அசுபதி" in stars
    assert "ரேவதி" in stars


def test_number_of_nakshatras():
    stars = list_nakshatras()

    assert len(stars) == len(NAKSHATRA_MAP)


# =========================================================
# EXCEPTION TESTS
# =========================================================

def test_invalid_nakshatra():
    with pytest.raises(ValueError):
        nakshatra_to_nazhi("XYZ")


# =========================================================
# MAP CONTENT TESTS
# =========================================================

def test_avittam_value():
    assert NAKSHATRA_MAP["அவிட்டம்"]["nazhi"] == 7


def test_revadhi_symbol():
    assert NAKSHATRA_MAP["ரேவதி"]["symbol"] == "பீடம்"


def test_anusham_nazhi():
    assert NAKSHATRA_MAP["அனுஷம்"]["nazhi"] == 6


# =========================================================
# UNKNOWN STAR IN TOTAL TEST
# =========================================================

def test_total_ignores_unknown_star():
    total = total_night_nazhi(
        ["அசுபதி", "XYZ"]
    )

    assert total == 2