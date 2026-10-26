from business_rules import (
    calculate_license_total,
    format_license_line,
    gets_trainer,
    largest_license,
    needs_contract_review,
    total_licensed,
)

orders = [
    {"company": "Pine Books", "seat_price": 40.00, "seats": 5, "education": False},
    {"company": "Quarry School", "seat_price": 35.00, "seats": 12, "education": True},
    {"company": "Redwood Cargo", "seat_price": 45.00, "seats": 60, "education": False},
    {"company": "Summit College", "seat_price": 50.00, "seats": 150, "education": True},
    {"company": "Tidal Health", "seat_price": 55.00, "seats": 100, "education": False},
    {"company": "Upland Farms", "seat_price": 60.00, "seats": 24, "education": False},
    {"company": "Vega Dental", "seat_price": 30.00, "seats": 25, "education": True},
    {"company": "Willow Law", "seat_price": 400.00, "seats": 9, "education": False},
]

order_count = 0
contract_review_count = 0
trainer_count = 0

print("Cloudstep Software - Order Report")

for order in orders:
    total = calculate_license_total(
        order["seat_price"], order["seats"], order["education"]
    )
    review = needs_contract_review(total)
    trainer = gets_trainer(order["seats"], total)

    print(format_license_line(order["company"], total, review, trainer))

    order_count += 1
    if review:
        contract_review_count += 1
    if trainer:
        trainer_count += 1

licensed_total = total_licensed(orders)
average_total = licensed_total / order_count
largest_company = largest_license(orders)

print(f"Orders: {order_count}")
print(f"Total licensed: ${licensed_total:.2f}")
print(f"Average license total: ${average_total:.2f}")
print(f"Largest license total: {largest_company}")
print(f"Contract reviews needed: {contract_review_count}")
print(f"Trainers assigned: {trainer_count}")
