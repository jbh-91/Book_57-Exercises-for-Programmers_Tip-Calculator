from icecream import ic
from math import floor, ceil

# Custom round function for educational purposes, usually just use "round(float_num, 2)
def round_to_2_decimals(float_num: float) -> float:
    # WONTFIX: Floating Point Math is wonky https://0.30000000000000004.com
    #          bill_amount = 11.25
    #          tip_rate = 10
    #          total_amount = 12.370000000000001
    if floor(float_num - 0.5) == int(float_num // 1):
        return ceil(float_num * 100) / 100
    else:
        return floor(float_num * 100) / 100


def calculate_tip_amount(amount: float | int, rate: int) -> float:
    return amount * rate / 100

def calculate_total_amount(bill_amount: float, tip: float) -> float:
    return tip + bill_amount


if __name__ == "__main__":
    bill_amount = float(input("Please enter your bill amount:\n> "))
    tip_rate = int(input("Please enter your tip rate (as percentage):\n> "))

    tip_amount = round_to_2_decimals(calculate_tip_amount(bill_amount, tip_rate))
    total_amount = calculate_total_amount(bill_amount, tip_amount)

    ic(f"{tip_amount} EUR")
    ic(f"{total_amount} EUR")
