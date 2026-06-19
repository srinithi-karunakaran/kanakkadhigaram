from kanakkadhigaram.alaviyal.neettal_alavai import (
    convert_length,
    list_length_units,
    list_viral_types,
    get_nel_count,
    get_viral_type,
    viral_to_muzham,
    muzham_to_viral,
    get_all_viral_mappings,
    saan_to_mulam,
    mulam_to_saan,
    explain_saan_conversion,
)


# =========================================================
# Length hierarchy
# =========================================================

def test_convert_length():

    assert convert_length(8, "அணு", "துகள்") == 1
    assert convert_length(8, "நெல்", "விரல்") == 1
    assert convert_length(2, "சாண்", "முழம்") == 1


def test_list_length_units():

    units = list_length_units()

    assert "அணு" in units
    assert "விரல்" in units
    assert "முழம்" in units
    assert "யோசனை" in units


# =========================================================
# Viral system
# =========================================================

def test_list_viral_types():

    types_ = list_viral_types()

    assert "உத்தம விரல்" in types_
    assert "மத்திம விரல்" in types_
    assert "அதம விரல்" in types_


def test_get_nel_count():

    assert get_nel_count("உத்தம விரல்") == 8
    assert get_nel_count("மத்திம விரல்") == 7
    assert get_nel_count("அதம விரல்") == 6


def test_get_viral_type():

    assert get_viral_type(8) == "உத்தம விரல்"
    assert get_viral_type(7) == "மத்திம விரல்"
    assert get_viral_type(6) == "அதம விரல்"


def test_viral_to_muzham():

    assert viral_to_muzham(9) == 1
    assert viral_to_muzham(18) == 2


def test_muzham_to_viral():

    assert muzham_to_viral(1) == 9
    assert muzham_to_viral(2) == 18


def test_get_all_viral_mappings():

    mapping = get_all_viral_mappings()

    assert mapping["உத்தம விரல்"] == 8
    assert mapping["மத்திம விரல்"] == 7
    assert mapping["அதம விரல்"] == 6


# =========================================================
# பாடல் 98
# =========================================================

def test_saan_to_mulam():

    result = saan_to_mulam(15)

    assert round(result, 2) == 312



def test_explain_saan_conversion():

    result = explain_saan_conversion(15)

    assert result["saan"] == 15
    assert result["viral_units"] == 180
    assert result["scaled"] == 1440
    assert result["correction"] == 36
    assert result["net"] == 1404
    assert result["mulam"] == 312