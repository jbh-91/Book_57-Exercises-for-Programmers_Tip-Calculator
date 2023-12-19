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


if __name__ == "__main__":
    unittest.main()
