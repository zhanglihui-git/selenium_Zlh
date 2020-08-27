from unittest import TestCase
from ddt import ddt, data, unpack
import  yaml
from src.Calc import Calc

@ddt
class TestCalc(TestCase):


    @data((1, 1, 2),
          (1, 0, 1),
          (1, -1, 0),
          (1, 1000000, 1000001)
          )
    @unpack
    def test_add(self, a, b, c):
        print(a, b, c)
        calc = Calc()
        result = calc.add(a, b)
        print("result=" + str(result))
        # assert result == 2
        self.assertEqual(result, c)
