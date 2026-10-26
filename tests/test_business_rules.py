from business_rules import (
    calculate_license_cost,
    calculate_license_total,
    format_license_line,
    get_seat_discount,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
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


def test_contract_review_below_limit():
    assert needs_contract_review(4999.99) is False


def test_contract_review_at_limit():
    assert needs_contract_review(5000.00) is False


def test_contract_review_above_limit():
    assert needs_contract_review(5000.01) is True


def test_trainer_below_seat_limit():
    assert gets_trainer(24, 1000.00) is False


def test_trainer_at_seat_limit():
    assert gets_trainer(25, 1000.00) is True


def test_trainer_below_limit():
    assert gets_trainer(1, 2999.99) is False


def test_trainer_at_total_limit():
    assert gets_trainer(1, 3000.00) is False


def test_trainer_above_total_limit():
    assert gets_trainer(1, 3000.01) is True


def test_trainer_when_both_conditions_qualify():
    assert gets_trainer(25, 3000.01) is True


def test_total_licensed_with_two_orders():
    orders = [
        {
            "company": "Pine Books",
            "seat_price": 40.00,
            "seats": 5,
            "education": False,
        },
        {
            "company": "Redwood Cargo",
            "seat_price": 45.00,
            "seats": 60,
            "education": False,
        },
    ]
    assert round(total_licensed(orders), 2) == 2771.00


def test_total_licensed_with_empty_list():
    assert round(total_licensed([]), 2) == 0.00


def test_largest_license_when_largest_is_in_middle():
    orders = [
        {
            "company": "Pine Books",
            "seat_price": 40.00,
            "seats": 5,
            "education": False,
        },
        {
            "company": "Redwood Cargo",
            "seat_price": 45.00,
            "seats": 60,
            "education": False,
        },
        {
            "company": "Quarry School",
            "seat_price": 35.00,
            "seats": 12,
            "education": True,
        },
    ]
    assert largest_license(orders) == "Redwood Cargo"


def test_format_line_with_neither_flag():
    assert format_license_line("Pine Books", 260.00, False, False) == (
        "Pine Books: $260.00 | contract review: no | trainer: no"
    )


def test_format_line_with_both_flags():
    assert format_license_line("Summit College", 6300.00, True, True) == (
        "Summit College: $6300.00 | contract review: yes | trainer: yes"
    )


def test_largest_license_returns_first_company_in_tie():
    orders = [
        {
            "company": "First Company",
            "seat_price": 40.00,
            "seats": 5,
            "education": False,
        },
        {
            "company": "Second Company",
            "seat_price": 40.00,
            "seats": 5,
            "education": False,
        },
    ]
    assert largest_license(orders) == "First Company"


def test_largest_license_with_empty_list():
    assert largest_license([]) == ""
