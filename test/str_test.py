# UnitTests for string.py Helper

import sys
import os
import unittest

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)

from string_utils import clean_number


class TestCleanNumber(unittest.TestCase):

    def test_clean_integer_string(self):
        self.assertEqual(clean_number("123"), 123.0)

    def test_clean_formatted_number(self):
        self.assertEqual(clean_number("-12,400 $"), -12400.0)

    def test_clean_float(self):
        self.assertEqual(clean_number(12.75), 12.75)

    def test_invalid_string(self):
        with self.assertRaises(ValueError):
            clean_number("abc xyz")

    def test_none_input(self):
        with self.assertRaises(ValueError):
            clean_number(None)


from string_utils import clean_name


class TestCleanName(unittest.TestCase):
    def test_clean_whitespace(self):
        self.assertEqual(clean_name("  John  "), "John")

    def test_title(self):
        self.assertEqual(clean_name("john"), "John")

    def test_is_str(self):
        with self.assertRaises(TypeError):
            clean_name(123)


if __name__ == "__main__":
    unittest.main()
