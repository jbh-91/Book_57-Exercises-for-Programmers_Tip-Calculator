import unittest
from tip_calculator import tip_calculator as tc

class TestTipMethods(unittest.TestCase):

    def test_basic_func(self):
        tip_amount = tc.calculate_tip_amount(10, 15)
        total_amount = tc.calculate_total_amount(10, tip_amount)
        self.assertEqual(tip_amount, 1.5)
        self.assertEqual(total_amount, 11.50)

    def test_tip_as_percentage(self):
        self.assertGreaterEqual(tc.calculate_tip_amount(10, 15), 0)
        self.assertIs(type(tc.calculate_tip_amount(10, 15)), float)

    def test_round(self):
        tip_amount = tc.round_to_2_decimals(tc.calculate_tip_amount(11.25, 15))
        total_amount = tc.calculate_total_amount(11.25, tip_amount)
        self.assertEqual(tip_amount, 1.69)
        self.assertEqual(total_amount, 12.94)

    def test_decimals(self):
        tip_amount = tc.round_to_2_decimals(tc.calculate_tip_amount(11.25, 15))
        total_amount = tc.calculate_total_amount(11.25, tip_amount)
        self.assertEqual(len(str(tip_amount).rsplit(".")[-1]), 2, "More or less than two decimal places")
        self.assertEqual(len(str(total_amount).rsplit(".")[-1]), 2, "More or less than two decimal places")

    def test_not_negative(self):
        tip_amount = tc.round_to_2_decimals(tc.calculate_tip_amount(10, -15))
        total_amount = tc.calculate_total_amount(10, tip_amount)
        self.assertGreater(tip_amount, 0, "Tip amount is negative")
        self.assertGreater(total_amount, 0, "Bill amount is negative")

    def test_total_larger_than_bill(self):
        tip_amount = tc.round_to_2_decimals(tc.calculate_tip_amount(10, 15))
        total_amount = tc.calculate_total_amount(10, tip_amount)
        self.assertGreater(total_amount, 10, "Bill amount is smaller than total amount")


if __name__ == "__main__":
    unittest.main()
