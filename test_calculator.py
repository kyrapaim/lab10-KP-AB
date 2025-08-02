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
        self.assertEqual(sub(1, 2), -1)
        self.assertEqual(sub(100, 500), -400)
        self.assertEqual(sub(-1, -20), 19)
    ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     self.assertEqual(self.calculator.mul(1, 2)
    #     self.assertEqual(self.calculator.mul(100, 500), 50000)
    #     self.assertEqual(self.calculator.mul(-1, -20), 20)
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    #     self.assertEqual(self.calculator.div(1, 2), 2.0)
    #     self.assertEqual(self.calculator.div(100, 500), 5.0)
    #     self.assertEqual(self.calculator.div(-1, -20), 20.0)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        # fill in code
        # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)


    def test_logarithm(self): # 3 assertions
        # fill in code
        with self.assertRaises(ValueError):
               log(0, 5)
        with self.assertRaises(ValueError):
               log(1, 5)
        with self.assertRaises(ValueError):
               log(-5, 5)

    def test_log_invalid_base(self): # 1 assertion
        # use same technique from test_divide_by_zero
        # fill in code
        with self.assertRaises(ZeroDivisionError):
               log(5, 0)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()