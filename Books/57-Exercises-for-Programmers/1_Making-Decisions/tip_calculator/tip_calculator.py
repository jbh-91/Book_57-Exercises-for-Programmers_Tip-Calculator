from math import floor, ceil
from string import digits

def check_input(check_string: str) -> bool:
    # negative value
    if "-" in check_string:
        return False
    
    # float check
    if "." in check_string:
        if len(check_string.split(".")) > 2:
            return False
        else:
            if not all([char in digits for char in "".join(check_string.split("."))]):
                return False
            return True
    
    # int check
    if not all([char in digits for char in check_string]):
        return False
    return True

def get_bill_and_tip_rate() -> tuple[float, int]:
    bill_amount = input("Please enter your bill amount:\n> ")
    while not check_input(bill_amount):
        bill_amount = input("Please enter a valid bill amount:\n> ")
        
    tip_rate = input("Please enter your tip rate (as percentage):\n> ")
    while not check_input(tip_rate):
        tip_rate = input("Please enter a valid tip rate (as percentage):\n> ")

    return float(bill_amount), int(tip_rate)

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

def render_bill(bill_amount: float, tip_rate: float) -> None:
    tip_amount = round_to_2_decimals(calculate_tip_amount(bill_amount, tip_rate))
    total_amount = calculate_total_amount(bill_amount, tip_amount)

    print(f"{tip_amount} EUR")
    print(f"{total_amount} EUR")

if __name__ == "__main__":
    bill_amount, tip_rate = get_bill_and_tip_rate()
    render_bill(bill_amount, tip_rate)
