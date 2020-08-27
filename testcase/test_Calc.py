from unittest import TestCase

from ddt import data

from src.Calc import Calc


@ddt
class TestCalc(TestCase):

    @data(1, 2, 3, 4, 5, 6)
    def test_demo(self, real):
        self.assertEqual(real, 5)

    def test_add(self):
        calc = Calc()
        result = calc.add(1, 1)
        # assert result == 2
        self.assertEqual(2, result)

    def test_div(self):
        calc = Calc()
        result = calc.div(2, 1)
        self.assertEqual(result, 2)

        result = calc
