# business_rules.py
# Author: Jean Carlos Reyes-Munoz


def calculate_license_cost(seat_price: float, seats: int) -> float:
    "Return the license cost before any discount."
    return seat_price * seats
