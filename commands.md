# Terminal Record: Cloudstep Software

## 1. Building the project
1. mkdir ism3232-midterm
2. mkdir -p tests
3. touch tests/__init__.py tests/test_business_rules.py
4. touch business_rules.py main.py commands.md README.md requirements.txt
5. pip install pytest ruff && pip freeze > requirements.txt
## 2. The virtual environment
/Users/jeancarlosreyes-munoz/ism3232-midterm/.venv/bin/python3
## 3. The project structure
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py
## 4. Every function and test
:def calculate_license_cost(seat_price: float, seats: int) -> float:
24:def get_seat_discount(seats: int, education: bool = False) -> float:
34:def calculate_license_total(
48:def needs_contract_review(total: float) -> bool:
53:def gets_trainer(seats: int, total: float) -> bool:
58:def total_licensed(orders: list) -> float:
70:def largest_license(orders: list) -> str:
87:def format_license_line(

tests/test_business_rules.py
13:def test_license_cost_one_seat():
17:def test_license_cost_multiple_seats():
21:def test_license_cost_zero_seats():
25:def test_license_cost_decimal_price():
29:def test_discount_below_first_tier():
33:def test_discount_at_first_tier():
37:def test_discount_below_education_tier():
41:def test_education_changes_top_tier_discount():
46:def test_license_total_below_fee_limit():
50:def test_license_total_at_fee_limit():
54:def test_license_total_above_fee_limit():
58:def test_onboarding_uses_discounted_cost():
62:def test_license_total_with_education_discount():
66:def test_contract_review_below_limit():
70:def test_contract_review_at_limit():
74:def test_contract_review_above_limit():
78:def test_trainer_below_seat_limit():
82:def test_trainer_at_seat_limit():
86:def test_trainer_below_limit():
90:def test_trainer_at_total_limit():
94:def test_trainer_above_total_limit():
98:def test_trainer_when_both_conditions_qualify():
102:def test_total_licensed_with_two_orders():
120:def test_total_licensed_with_empty_list():
124:def test_largest_license_when_largest_is_in_middle():
148:def test_format_line_with_neither_flag():
154:def test_format_line_with_both_flags():
160:def test_largest_license_returns_first_company_in_tie():
178:def test_largest_license_with_empty_list():

The file business_rules.py defines eight functions, and tests/test_business_rules.py defines 29 tests.
## 5. Which files print
main.py
main.py prints the report. business_rules.py is not listed because its functions return values instead of printing them.
## 6. The commit history
8111a13 (HEAD -> main) Fix order count and add largest license tests
7de8420 Add Cloudstep Software order report
8b83438 Add license summary loops and report formatting with test
12458e5 Add contract review and trainer rules with tests
8088714 Add trial seat discount and license total with tests
8a8ffb9 Add license cost calculation and test
2beee6a ism3232-midterm setup
(END)
There are 6 commits at this point.