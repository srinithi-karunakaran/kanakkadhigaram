from kanakkadhigaram.enn_arithal import *


# =========================================================
# PERU EN SCALE TESTS
# =========================================================

def test_convert_peru_en():
    result = convert_peru_en(1, "கற்பம்", "அணு")

    assert result > 0


def test_list_peru_en_units():
    units = list_peru_en_units()

    assert "கற்பம்" in units
    assert "அணு" in units


# =========================================================
# SAARAM SCALE TESTS
# =========================================================

def test_convert_saaram():
    result = convert_saaram(5, "இம்மி", "நுட்பம்")

    assert result > 0


def test_list_saaram_units():
    units = list_saaram_units()

    assert "அதிசாரம்" in units
    assert "முந்திரிகை" in units


# =========================================================
# MUNDHIRI SCALE TESTS
# =========================================================

def test_convert_mundhiri():
    result = convert_mundhiri(1, "மேல் முந்திரி", "சின்னம்")

    assert result > 0


def test_list_mundhiri_units():
    units = list_mundhiri_units()

    assert "சின்னம்" in units
    assert "ஒன்று" in units


# =========================================================
# KANI SCALE TESTS
# =========================================================

def test_convert_kani():
    result = convert_kani(1, "ஒன்று", "முந்திரிகை")

    assert result == 320


def test_convert_kani_ma_to_kani():
    result = convert_kani(1, "மா", "காணி")

    assert result == 4


def test_list_kani_units():
    units = list_kani_units()

    assert "ஒன்று" in units
    assert "முந்திரிகை" in units


# =========================================================
# COMMON ENGINE TESTS
# =========================================================

def test_build_base_values():
    sample = {
        "A": {"next": "B", "factor": 2},
        "B": {"next": "C", "factor": 5}
    }

    values = build_base_values(sample, "C")

    assert values["C"] == 1
    assert values["B"] == 5
    assert values["A"] == 10


def test_convert_system():
    base = {
        "A": 10,
        "B": 5,
        "C": 1
    }

    result = convert_system(1, "A", "C", base)

    assert result == 10


# =========================================================
# EXCEPTION TESTS
# =========================================================

import pytest


def test_invalid_peru_en_unit():
    with pytest.raises(ValueError):
        convert_peru_en(1, "XYZ", "அணு")


def test_invalid_saaram_unit():
    with pytest.raises(ValueError):
        convert_saaram(1, "ABC", "முந்திரிகை")


def test_invalid_mundhiri_unit():
    with pytest.raises(ValueError):
        convert_mundhiri(1, "ABC", "ஒன்று")


def test_invalid_kani_unit():
    with pytest.raises(ValueError):
        convert_kani(1, "ABC", "முந்திரிகை")