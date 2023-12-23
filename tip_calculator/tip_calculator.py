from math import floor, ceil
from string import digits

def check_input(check_string: str, allow_zero: bool = False) -> bool | int | float:
    if not allow_zero and check_string == "0":
        return False
    
    # empty string
    if check_string is "":
        return False
    
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
            return float(check_string)
    
    # int check
    if not all([char in digits for char in check_string]):
        return False
    return int(check_string)

def get_input(input_var_name: str, allow_zero: bool) -> float | int:
    user_input = check_input(input(f"Please enter your {input_var_name}:\n> "), allow_zero)
    while user_input is False:
        user_input = check_input(input(f"Please enter a valid {input_var_name}:\n> "), allow_zero)

    return user_input

# Custom round function for educational purposes, usually just use round(float_num, 2)
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

    print(f"{tip_amount=:.2f} EUR")
    print(f"{total_amount=:.2f} EUR")

if __name__ == "__main__":
    bill_amount = get_input("bill amount")
    tip_rate = get_input("tip rate (as percentage)", allow_zero=True)

    render_bill(bill_amount, tip_rate)
