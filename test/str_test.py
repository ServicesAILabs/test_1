
# UnitTests for string.py Helper

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
print(sys.path)

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

if __name__ == '__main__':
    unittest.main()