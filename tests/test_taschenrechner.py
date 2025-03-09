# pylint: disable=C0114, C0115, C0116
import importlib as il
from unittest import TestCase

calculator = il.import_module(
    "Exercises.03Taschenrechner.mitTests(TestDrivenDevelopment).main"
)
calculate = calculator.taschenrechner


class TestCalculator(TestCase):
    def test_zero_add_zero(self):
        expected_result = 0
        result = calculate(0, 0, "+")

        self.assertEqual(expected_result, result)

    def test_zero_multiply_zero(self):
        expected_result = 0
        result = calculate(0, 0, "*")

        self.assertEqual(expected_result, result)

    def test_one_multiply_minus_two(self):
        expected_result = -1
        result = calculate(1, -2, "+")

        self.assertEqual(expected_result, result)

    def test_invalid_operator(self):
        expected_result = None
        result = calculate(0, 0, "#")

        self.assertEqual(expected_result, result)

    def test_zero_division(self):
        expected_result = None
        result = calculate(100, 0, "/")

        self.assertEqual(expected_result, result)

    def test_ten_multiply_ten(self):
        expected_result = 100
        result = calculate(10, 10, "*")

        self.assertEqual(expected_result, result)

    def test_ten_add_five(self):
        expected_result = 15
        result = calculate(10, 5, "+")

        self.assertEqual(expected_result, result)

    def test_onehundredandfifty_minus_fifty(self):
        expected_result = 100
        result = calculate(150, 50, "-")

        self.assertEqual(expected_result, result)
