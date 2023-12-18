from icecream import ic

def round_up(float_num: float) -> float:
    # TODO: Custom round function for educational purposes
    # if float_num - 0.5 == float_num:
    
    return round(float_num, 2)

def calculate_tip_amount(amount: float | int, rate: int) -> float:
    return amount * rate / 100

def calculate_total_amount(bill_amount: float, tip: float) -> float:
    return tip + bill_amount


if __name__ == "__main__":
    bill_amount = float(input())
    tip_rate = int(input())
    
    tip_amount = calculate_tip_amount(bill_amount, tip_rate)

    total_amount = calculate_total_amount(bill_amount, tip_amount)
    ic(f"{tip_amount:.2f} EUR")
    ic(f"{total_amount:.2f} EUR")