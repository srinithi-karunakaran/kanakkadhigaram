from kanakkadhigaram.porul_alavai.vennkalam_pithalai_seythal import (
    venkalam_ratio,
    pithalai_ratio,
    identify_metal,
)


# ==========================================================
# வெண்கலம் கணக்கு
# ==========================================================

def test_venkalam_ratio():

    result = venkalam_ratio(8)

    assert result["copper"] == 8
    assert result["tin"] == 2
    assert result["alloy"] == 10


# ==========================================================
# பித்தளை கணக்கு
# ==========================================================

def test_pithalai_ratio():

    result = pithalai_ratio(7.5)

    assert result["copper"] == 7.5
    assert result["tin"] == 3
    assert result["alloy"] == 10.5


# ==========================================================
# கலவை வகை கண்டறிதல்
# ==========================================================

def test_identify_venkalam():

    assert identify_metal(8, 2) == "வெண்கலம் (Bronze)"


def test_identify_pithalai():

    assert identify_metal(7.5, 3) == "பித்தளை (Brass)"


def test_unknown_metal():

    assert identify_metal(10, 1) == "தெரியாத கலவை"