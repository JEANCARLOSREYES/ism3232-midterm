# business_rules.py
# Author: Jean Carlos Reyes-Munoz

NO_DISCOUNT_RATE = 0.00
STANDARD_DISCOUNT_RATE = 0.07
EDUCATION_DISCOUNT_RATE = 0.16

MID_TIER_SEATS = 10
TOP_TIER_SEATS = 50

ONBOARDING_COST_LIMIT = 400.00
ONBOARDING_FEE = 60.00

CONTRACT_REVIEW_LIMIT = 5000.00
TRAINER_SEAT_LIMIT = 25
TRAINER_TOTAL_LIMIT = 3000.00


def calculate_license_cost(seat_price: float, seats: int) -> float:
    "Return the license cost before any discount."
    return seat_price * seats


def get_seat_discount(seats: int, education: bool = False) -> float:
    "Return the discount rate as a decimal, so 7% is 0.07."
    if seats >= TOP_TIER_SEATS and education:
        return EDUCATION_DISCOUNT_RATE
    elif seats >= MID_TIER_SEATS:
        return STANDARD_DISCOUNT_RATE
    else:
        return NO_DISCOUNT_RATE


def calculate_license_total(
    seat_price: float, seats: int, education: bool = False
) -> float:
    "Return the discounted license cost plus any onboarding fee."
    cost = calculate_license_cost(seat_price, seats)
    discount = get_seat_discount(seats, education)
    discounted_cost = cost - cost * discount

    if discounted_cost <= ONBOARDING_COST_LIMIT:
        discounted_cost += ONBOARDING_FEE

    return discounted_cost
