from unittest import TestCase

from kata_1 import add


class Tests(TestCase):

    def test_empty_string_return_zero(self):
        self.assertEqual(0, add(''))

    def test_method_returns_eleven(self):
        self.assertEqual(11, add('11'))

    def test_method_returns_fifteen(self):
        self.assertEqual(15, add('1,14'))

    def test_method_returns_twalve(self):
        self.assertEqual(12, add('4,6,2'))

    def test_method_with_new_lines_returns_twenty(self):
        self.assertEqual(20, add('1\n7,1\n11'))

    def test_different_delimiters_returns_six(self):
        self.assertEqual(6, add('//[;]\n4;2'))

    def test_raise_error_with_negative_values(self):
        with self.assertRaises(ValueError):
            add('//j\n2j-5j2j-12')

    def test_numbers_bigger_then_one_thousand_are_omitted(self):
        self.assertEqual(15, add('1001\n2,2500,13966\n12,1'))

    def test_any_lenght_of_delimiters(self):
        self.assertEqual(6, add('//[***]\n1***2***3'))

    def test_multiple_delimiters_returns_six(self):
        self.assertEqual(6, add('//[*][%]\n1*2%3'))
