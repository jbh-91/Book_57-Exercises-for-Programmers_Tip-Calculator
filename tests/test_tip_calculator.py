import unittest
from tip_calculator import tip_calculator

class TestTipMethods(unittest.TestCase):

    def test_basic_func(self):
        tc = tip_calculator.TipCalculator(10, 15)
        self.assertEqual(tc.tip_amount, 1.5)
        self.assertEqual(tc.total_amount, 11.50)

    def test_tip_as_percentage(self):
        tc = tip_calculator.TipCalculator(10, 15)
        self.assertGreaterEqual(tc.tip_amount, 0)
        self.assertIs(type(tc.tip_amount), float)

    def test_rounding(self):
        tc = tip_calculator.TipCalculator(11.25, 15)
        self.assertEqual(tc.tip_amount, 1.69)
        self.assertEqual(tc.total_amount, 12.94)

    def test_decimals(self):
        tc = tip_calculator.TipCalculator(11.25, 15)
        self.assertEqual(len(str(tc.tip_amount).rsplit(".")[-1]), 2, "More or less than two decimal places")
        self.assertEqual(len(str(tc.total_amount).rsplit(".")[-1]), 2, "More or less than two decimal places")

    def test_input_not_negative(self):
        tc = tip_calculator.TipCalculator()
        self.assertFalse(tc.check_string_input("-15"), "Tip rate is negative")
        self.assertFalse(tc.check_string_input("-11.25"), "Bill amount is negative")

    def test_total_larger_than_bill(self):
        tc = tip_calculator.TipCalculator(10, 15)
        self.assertGreater(tc.total_amount, 10, "Bill amount is smaller than total amount")


if __name__ == "__main__":
    unittest.main()
