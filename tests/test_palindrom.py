# pylint: disable=C0114, C0115, C0116
from unittest import TestCase

from Exercises._01Palindrom.main import palindrom as is_palindrom


class TestPalindrom(TestCase):
    def test_empty_string(self):
        expected_result = False
        result = is_palindrom("")

        self.assertEqual(expected_result, result)

    def test_lower_upper_aa(self):
        expected_result = True
        result = is_palindrom("aA")

        self.assertEqual(expected_result, result)

    def test_busfahrt(self):
        expected_result = False
        result = is_palindrom("Busfahrt")

        self.assertEqual(expected_result, result)

    def test_rentner(self):
        expected_result = True
        result = is_palindrom("Rentner")

        self.assertEqual(expected_result, result)

    def test_amok_oma(self):
        expected_result = True
        result = is_palindrom("Amok Oma")

        self.assertEqual(expected_result, result)

    def test_ein_esel_lese_nie(self):
        expected_result = True
        result = is_palindrom("Ein Esel lese nie")

        self.assertEqual(expected_result, result)
