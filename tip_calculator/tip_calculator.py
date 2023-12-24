"""Simple Tip Calculator

This module contains the class TipCalculator, which is a simple tool to calculate the tip and total bill amount based on an input tip rate and an input bill amount. The class also allows the input from and output to the command line interface.

Example:
    To use the TipCalculator class, create an instance of the class and optionally pass
    - a float or integer value for the bill amount
    - an integer value for the tip rate
    OR
    - a boolean value that indicates whether you want to get the input from the command line interface or not. By default, this value is False.

    >>> tip_calculator = TipCalculator(input_from_cli=True)
    Please enter your bill amount:
    > 50
    Please enter your tip rate (as percentage):
    > 15
    >>> tip_calculator.render_bill_in_cli()
    tip_amount=7.50 EUR
    total_amount=57.50 EUR
"""

# Standard library imports
from math import floor, ceil
from string import digits

class TipCalculator():

    def __init__(self, bill_amount: float | str = 0, tip_rate: int | str = 0, input_from_cli: bool = False) -> None:
        if input_from_cli:
            self.bill_amount = self.get_input_from_cli("bill amount")
            self.tip_rate = self.get_input_from_cli("tip rate (as percentage)", allow_zero=True, allow_float=False)
        else:
            self.bill_amount: float = bill_amount
            self.tip_rate: int = tip_rate

        self.tip_amount: float = self.round_to_2_decimals(self.bill_amount * self.tip_rate / 100)
        self.total_amount: float = self.tip_amount + self.bill_amount


    def check_string_input(self, string_to_check: str, allow_zero: bool = False, allow_float: bool = True) -> bool | int | float:
        if not allow_zero and string_to_check == "0":
            return False
        
        # empty string
        if string_to_check is "":
            return False
        
        # negative value
        if "-" in string_to_check:
            return False
        
        # float check
        if "." in string_to_check and allow_float:
            if len(string_to_check.split(".")) > 2:
                return False
            else:
                if not all([char in digits for char in "".join(string_to_check.split("."))]):
                    return False
                return float(string_to_check)
        
        # int check
        if not all([char in digits for char in string_to_check]):
            return False
        return int(string_to_check)

    def round_to_2_decimals(self, float_num: float) -> float:
        # Custom round function for educational purposes, usually just use round(float_num, 2)
        # WONTFIX: Floating Point Math is wonky https://0.30000000000000004.com
        #          bill_amount = 11.25
        #          tip_rate = 10
        #          total_amount = 12.370000000000001
        if floor(float_num - 0.5) == int(float_num // 1):
            return ceil(float_num * 100) / 100
        else:
            return floor(float_num * 100) / 100

    def get_input_from_cli(self, input_var_name: str, allow_zero: bool = False, allow_float: bool = True) -> float | int:
        user_input = self.check_string_input(input(f"Please enter your {input_var_name}:\n> "), allow_zero, allow_float)
        while user_input is False:
            user_input = self.check_string_input(input(f"Please enter a valid {input_var_name}:\n> "), allow_zero, allow_float)

        return user_input

    def render_bill_in_cli(self) -> None:
        print(f"{self.tip_rate=} %")
        print(f"{self.bill_amount=:.2f} EUR")
        print(f"{self.tip_amount=:.2f} EUR")
        print(f"{self.total_amount=:.2f} EUR")


if __name__ == "__main__":
    tc = TipCalculator(input_from_cli=True)
    tc.render_bill_in_cli()
