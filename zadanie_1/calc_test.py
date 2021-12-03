import unittest
from calc import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.object = Calculator()

    def tearDown(self):
        del self.object

    def test_addition_two_positive_numbers(self):
        result = self.object.addition(1, 2)
        self.assertEqual(3, result)

    def test_addition_two_negative_numbers(self):
        result = self.object.addition(-1, -2)
        self.assertEqual(-3, result)

    def test_addition_negative_and_positive_numbers(self):
        result = self.object.addition(-1, 2)
        self.assertEqual(1, result)

    def test_subtraction_two_positive_numbers(self):
        result = self.object.subtraction(45, 2)
        self.assertEqual(43, result)

    def test_subtraction_two_negative_numbers(self):
        result = self.object.subtraction(-45, -2)
        self.assertEqual(-43, result)

    def test_subtraction_negative_and_positive_numbers(self):
        result = self.object.subtraction(-45, 2)
        self.assertEqual(-47, result)

    def test_addition_negative_number_with_bad_type(self):
        result = self.object.addition(1, 'a')
        warn = f"{type(1)} a={1} | {type('a')} b={'a'} \n Both should be <class 'int'>"
        self.assertTrue(result, warn)

    def test_addition_when_numbers_are_string(self):
        result = self.object.addition('a', 'a')
        self.assertNotEqual(1, result)

    def test_subtraction_when_number_are_float(self):
        result = self.object.subtraction(1, 1.2)
        warn = f"{type(1)} a={1} | {type('a')} b={'a'} \n Both should be <class 'int'>"
        self.assertTrue(result, warn)
