# https://github.com/kyrapaim/lab10-KP-AB.git
# Partner 1: Kyra Paim
# Partner 2: Amkia Beaton

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        # fill in code
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(100, 500), 600)
        self.assertEqual(add(-1, -20), -21)

    def test_subtract(self): # 3 assertions
        # fill in code
        self.assertEqual(subtract(1, 2), -1)
        self.assertEqual(subtract(100, 500), -400)
        self.assertEqual(subtract(-1, -20), 19)
    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(10, 10),100)
        self.assertNotEqual(mul(-10, -10),-10)



    def test_divide(self): # 3 assertions
        self.assertNotEqual(div(5, 2), 5)
        self.assertEqual(div(100, 500), 5)
        self.assertEqual(div(8, 64), 8)


    def test_divide_by_zero(self): # 1 assertion
        # fill in code
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        # fill in code
        with self.assertRaises(ValueError):
               logarithm(0, 5)
        with self.assertRaises(ValueError):
               logarithm(1, 5)
        with self.assertRaises(ValueError):
               logarithm(-5, 5)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        # fill in code
        with self.assertRaises(ZeroDivisionError):
               logarithm(5, 0)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertNotEqual(hypotenuse(2,2), 600)
        self.assertEqual(hypotenuse(4,3), 5)
        self.assertAlmostEqual(hypotenuse(2,2), 2.82842712474619047)


    def test_square_root(self): # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(25), 5)


# Do not touch this
if __name__ == "__main__":
    unittest.main()