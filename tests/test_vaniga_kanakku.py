from fractions import Fraction

from kanakkadhigaram.vaniga_kanakku.ponn import (
    proportional_transform,
    relation_structure,
    cumulative_sum_transform,
    product_scale_transform,
    add_remove_balance,
    weighted_square_transform,
    average_like_merge,
    normalized_square_merge,
    difference_extraction,
    scale_conversion,
    additive_adjustment,
    weighted_distribution
)


# =========================================================
# பாடல் 183
# =========================================================

def test_proportional_transform():

    result = proportional_transform(10)

    assert result["input"] == 10
    assert result["step_1"] == 20
    assert result["step_2"] == 2.5


# =========================================================
# பாடல் 184
# =========================================================

def test_relation_structure():

    result = relation_structure()

    assert "swap_relation" in result["operations"]
    assert len(result["operations"]) == 4


# =========================================================
# பாடல் 185
# =========================================================

def test_cumulative_sum_transform():

    result = cumulative_sum_transform()

    assert result["sum"] == 40
    assert result["scaled"] == 40000
    assert result["result"] == 1000


# =========================================================
# பாடல் 186
# =========================================================

def test_product_scale_transform():

    result = product_scale_transform(10, 5)

    assert result["gold"] == 10
    assert result["silver"] == 5
    assert result["product"] == 50
    assert result["scaled"] == 5


# =========================================================
# பாடல் 187
# =========================================================

def test_add_remove_balance():

    result = add_remove_balance(20)

    assert result["added"] == Fraction(10, 1)
    assert result["removed"] == Fraction(5, 1)
    assert result["result"] == 25


# =========================================================
# பாடல் 188
# =========================================================

def test_weighted_square_transform():

    result = weighted_square_transform()

    assert result["total"] == 330
    assert result["result"] == 8.25


# =========================================================
# பாடல் 189
# =========================================================

def test_average_like_merge():

    result = average_like_merge([10, 9, 8])

    assert result["sum"] == 27
    assert result["reduced"] == 9


# =========================================================
# பாடல் 190
# =========================================================

def test_normalized_square_merge():

    result = normalized_square_merge([10, 9, 8])

    assert result["weighted"] == [100, 81, 64]
    assert result["result"] == 81.66666666666667


# =========================================================
# பாடல் 191
# =========================================================

def test_difference_extraction():

    result = difference_extraction(10, 15)

    assert result["difference"] == 5


# =========================================================
# பாடல் 192
# =========================================================

def test_scale_conversion():

    result = scale_conversion(10)

    assert result["scaled"] == Fraction(8, 1)


# =========================================================
# பாடல் 193
# =========================================================

def test_additive_adjustment():

    result = additive_adjustment(10)

    assert result["result"] == 13


# =========================================================
# பாடல் 194
# =========================================================

def test_weighted_distribution():

    result = weighted_distribution()

    distribution = result["distribution"]

    assert distribution[10] == Fraction(250, 1)
    assert distribution[9] == Fraction(225, 1)
    assert distribution[8] == Fraction(200, 1)
    assert distribution[7] == Fraction(175, 1)
    assert distribution[6] == Fraction(150, 1)