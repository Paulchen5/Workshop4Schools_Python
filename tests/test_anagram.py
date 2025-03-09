# pylint: disable=C0114, C0115, C0116
import importlib as il

from unittest import TestCase

anagram = il.import_module("Exercises.02Anagramm.main")
is_anagram = anagram.anagramm


class TestAnagram(TestCase):
    def test_empty_string(self):
        expected_result = False
        result = is_anagram("", "")

        self.assertEqual(expected_result, result)

    def test_lower_a(self):
        expected_result = True
        result = is_anagram("a", "a")

        self.assertEqual(expected_result, result)

    def test_ab(self):
        expected_result = False
        result = is_anagram("ab", "b")

        self.assertEqual(expected_result, result)

    def test_upper_a(self):
        expected_result = True
        result = is_anagram("A", "a")

        self.assertEqual(expected_result, result)

    def test_auu(self):
        expected_result = True
        result = is_anagram("Auu", "UAu")

        self.assertEqual(expected_result, result)

    def test_mehl(self):
        expected_result = True
        result = is_anagram("Mehl", "Lehm")

        self.assertEqual(expected_result, result)

    def test_aberglaube(self):
        expected_result = True
        result = is_anagram("Aberglaube", "Regelabbau")

        self.assertEqual(expected_result, result)

    def test_bauschutt(self):
        expected_result = True
        result = is_anagram("bauschutt", "Staubtuch")

        self.assertEqual(expected_result, result)
