from business_rules import calculate_license_cost


def test_license_cost_one_seat():
    assert round(calculate_license_cost(35.00, 1), 2) == 35.00


def test_license_cost_multiple_seats():
    assert round(calculate_license_cost(40.00, 5), 2) == 200.00


def test_license_cost_zero_seats():
    assert round(calculate_license_cost(40.00, 0), 2) == 0.00


def test_license_cost_decimal_price():
    assert round(calculate_license_cost(12.50, 3), 2) == 37.50
