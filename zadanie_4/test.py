import unittest
from unittest.mock import patch
from example import Example


class ExampleTest(unittest.TestCase):
    def test_example(self):
        example = Example()

        a = example.a()
        self.assertEqual(0, a)

    @patch('example.Example.b', return_value=0)
    def test_example2(self, mocked):
        example = Example()

        b = example.b()
        mocked.assert_called_once()
        self.assertEqual(0, b)

    @patch('example.Example.b', return_value="example")
    def test_example3(self, mocked):
        example = Example()

        b = example.b()
        mocked.assert_called_once()
        self.assertEqual("example", b)

    @patch('example.Example.b', return_value=2.3)
    def test_example4(self, mocked):
        example = Example()

        b = example.b()
        mocked.assert_called_once()
        self.assertEqual(2.3, b)


class CalcTest(unittest.TestCase):
    @patch('calc.Calculator.addition', return_value=5)
    def test_addition(self, mocked):
        self.assertEqual(mocked(2, 3), 5)

    @patch('calc.Calculator.subtraction', return_value=1)
    def test_subtraction(self, mocked):
        self.assertEqual(mocked(2, 1), 1)

    @patch('calc.Calculator.subtraction', return_value=('string', 1.3))
    def test_subtraction_tuple(self, mocked):
        self.assertEqual(mocked(10, 5), ('string', 1.3))
