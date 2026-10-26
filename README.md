# ISM3232 Midterm: Cloudstep Software

- **Name:** Jean Carlos Reyes-Munoz
- **Version:** EPISILON
- **Date:** October 25, 2026

## What This Program Does
This program calculates software license totals for 8 customer orders. It applies discounts and onboarding fees then identifies orders that need a contract reivew or dedicated trainer. It print each order and a summary showing counts, totals, the average and the largest order.
## Business Rules
1. The starting license cost is the prie per seat multiplied by the number of seats.
2. Orders below 10 seats receive no discount. Order of 10 through 49 seats receive 7%, while orders of 50 or more may receive 16% under the education rule.
3. The 16% discount is only for education people. Other orders of 50 or more seats receive 7%.
4. Add a $60 onboarding fee when the discounted cost is $400 or less.
5. A final total greater than $5000 requires a contract review.
6. An order gets a trainer when it has at least 25 seats or a final total greater than $3000.
## How to Run
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install requirements.txt
python3 main.py
## How to Test
ruff format .
ruff check .
pytest -v
The project has 29 tests covering all 8 functions.
## Files in This Repository
bsuiness_rules.py
main.py
tests/test__init__.py
tests/test_business_rules.py
commands.md
README.md
requirements.txt
.gitignore
## AI Use Statement
I did not use AI while completing this midterm.