from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    get_seat_discount,
)


def test_license_cost_one_seat():
    assert round(calculate_license_cost(35.00, 1), 2) == 35.00


def test_license_cost_multiple_seats():
    assert round(calculate_license_cost(40.00, 5), 2) == 200.00


def test_license_cost_zero_seats():
    assert round(calculate_license_cost(40.00, 0), 2) == 0.00


def test_license_cost_decimal_price():
    assert round(calculate_license_cost(12.50, 3), 2) == 37.50


def test_discount_below_first_tier():
    assert get_seat_discount(9) == 0.00


def test_discount_at_first_tier():
    assert get_seat_discount(10) == 0.07


def test_discount_below_education_tier():
    assert get_seat_discount(49, education=True) == 0.07


def test_education_changes_top_tier_discount():
    assert get_seat_discount(50, education=False) == 0.07
    assert get_seat_discount(50, education=True) == 0.16


def test_license_total_below_fee_limit():
    assert round(calculate_license_total(399.99, 1), 2) == 459.99


def test_license_total_at_fee_limit():
    assert round(calculate_license_total(400.00, 1), 2) == 460.00


def test_license_total_above_fee_limit():
    assert round(calculate_license_total(400.01, 1), 2) == 400.01


def test_onboarding_uses_discounted_cost():
    assert round(calculate_license_total(43.00, 10), 2) == 459.90


def test_license_total_with_education_discount():
    assert round(calculate_license_total(10.00, 50, education=True), 2) == 420.00
