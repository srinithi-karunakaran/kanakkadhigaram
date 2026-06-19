from fractions import Fraction

from kanakkadhigaram.vivasaya_kanakku.nell import (
    grain_volume_conversion,
    grain_price_estimation,
    fractional_grain_conversion,
    trade_profit_analysis,
)


# =========================================================
# பாடல் 201
# =========================================================

def test_grain_volume_conversion():

    result = grain_volume_conversion(1)

    assert result["கலம்"] == "1 கலம்"
    assert result["மரக்கால்"] == "3 மரக்கால்"
    assert result["உழக்கு"] == "12 உழக்கு"
    assert result["ஆழாக்கு"] == "6.0 ஆழாக்கு"


# =========================================================
# பாடல் 202
# =========================================================

def test_grain_price_estimation():

    result = grain_price_estimation(80, 20)

    assert result["நெல் அளவு"] == "80 அளவு"
    assert result["ஒரு அலகு விலை"] == "20 பணம்"
    assert result["மொத்த மதிப்பு"] == "1600 பணம்"
    assert result["சீரமைக்கப்பட்ட மதிப்பு"] == "80.0 பணம்"


# =========================================================
# பாடல் 203
# =========================================================

def test_fractional_grain_conversion():

    result = fractional_grain_conversion()

    expected = Fraction(1, 2) + Fraction(1, 4) + Fraction(1, 20)

    assert result["மொத்த பகுதி"] == f"{expected} (fractional அளவு)"


# =========================================================
# பாடல் 204
# =========================================================

def test_trade_profit_analysis_profit():

    result = trade_profit_analysis(10, 15)

    assert result["வாங்கிய விலை"] == "10 பணம்"
    assert result["விற்ற விலை"] == "15 பணம்"
    assert result["விலை வேறுபாடு"] == "5 பணம்"
    assert result["விகிதம்"] == str(10 / 15)


def test_trade_profit_analysis_loss():

    result = trade_profit_analysis(20, 10)

    assert result["வாங்கிய விலை"] == "20 பணம்"
    assert result["விற்ற விலை"] == "10 பணம்"
    assert result["விலை வேறுபாடு"] == "10 பணம்"
    assert result["விகிதம்"] == str(20 / 10)


def test_trade_profit_analysis_zero_division():

    result = trade_profit_analysis(20, 0)

    assert result["விகிதம்"] == "None"