from solutions.CHK import checkout_solution
import unittest


class TestCheckout(unittest.TestCase):
    def test_single_prices(self):
        self.assertEqual(checkout_solution.checkout(''), 0)
        self.assertEqual(checkout_solution.checkout('A'), 50)
        self.assertEqual(checkout_solution.checkout('B'), 30)
        self.assertEqual(checkout_solution.checkout('C'), 20)
        self.assertEqual(checkout_solution.checkout('D'), 15)
        self.assertEqual(checkout_solution.checkout('E'), 40)

    def test_special_offers(self):
        self.assertEqual(checkout_solution.checkout('AAA'), 130)
        self.assertEqual(checkout_solution.checkout('BB'), 45)
        self.assertEqual(checkout_solution.checkout('EE'), 80)
        self.assertEqual(checkout_solution.checkout('EEB'), 80)
        self.assertEqual(checkout_solution.checkout('EEBB'), 110) #favour customer
        self.assertEqual(checkout_solution.checkout('EEBBB'), 125)
        self.assertEqual(checkout_solution.checkout('AAAAA'), 200)
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)
        self.assertEqual(checkout_solution.checkout('ACAA'), 150)
        self.assertEqual(checkout_solution.checkout('ABABA'), 175)

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.checkout('a'), -1)
        self.assertEqual(checkout_solution.checkout('-'), -1)
        self.assertEqual(checkout_solution.checkout('ABCa'), -1)




