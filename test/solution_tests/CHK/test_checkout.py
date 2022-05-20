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
        self.assertEqual(checkout_solution.checkout('F'), 10)
 
    def test_special_offers(self):
        self.assertEqual(checkout_solution.checkout('AAA'), 130)
        self.assertEqual(checkout_solution.checkout('BB'), 45)
        self.assertEqual(checkout_solution.checkout('EE'), 80)
        self.assertEqual(checkout_solution.checkout('FF'), 20)
        self.assertEqual(checkout_solution.checkout('FFF'), 20)
        self.assertEqual(checkout_solution.checkout('EEB'), 80)
        self.assertEqual(checkout_solution.checkout('EEBB'), 110) #favour customer
        self.assertEqual(checkout_solution.checkout('EEBBB'), 125)
        self.assertEqual(checkout_solution.checkout('EEEEBB'), 160)
        self.assertEqual(checkout_solution.checkout('BEBEEE'), 160)
        self.assertEqual(checkout_solution.checkout('AAAAAA'), 250)
        self.assertEqual(checkout_solution.checkout('ACAA'), 150)
        self.assertEqual(checkout_solution.checkout('ABABA'), 175)
        self.assertEqual(checkout_solution.checkout('FFFF'), 30)
        self.assertEqual(checkout_solution.checkout('FFFFF'), 40)
        self.assertEqual(checkout_solution.checkout('FFFFFF'), 40)
        self.assertEqual(checkout_solution.checkout('AFAFAF'), 150)
        self.assertEqual(checkout_solution.checkout('HHHHHHHHHH'), 80)
        self.assertEqual(checkout_solution.checkout('AFAFAF'), 150)
        self.assertEqual(checkout_solution.checkout('AFAFAF'), 150)
        self.assertEqual(checkout_solution.checkout('AFAFAF'), 150)
        self.assertEqual(checkout_solution.checkout('AFAFAF'), 150)
        self.assertEqual(checkout_solution.checkout('AFAFAF'), 150)
        self.assertEqual(checkout_solution.checkout('AFAFAF'), 150)
 
    def test_GroupPricer(self):
        self.assertEqual(checkout_solution.checkout('SSS'), 45)
        self.assertEqual(checkout_solution.checkout('TTT'), 45)
        self.assertEqual(checkout_solution.checkout('XXX'), 45)
        self.assertEqual(checkout_solution.checkout('YYY'), 45)
        self.assertEqual(checkout_solution.checkout('ZZZ'), 45)
        self.assertEqual(checkout_solution.checkout('SXY'), 45)
        self.assertEqual(checkout_solution.checkout('ZYX'), 45)
        self.assertEqual(checkout_solution.checkout('ZYX'), 45)
        self.assertEqual(checkout_solution.checkout('ABCZYX'), 145)
        self.assertEqual(checkout_solution.checkout('UUUUZYX'), 165)
        self.assertEqual(checkout_solution.checkout('NNNMZYX'), 165)
        self.assertEqual(checkout_solution.checkout('ZYXX'), 62) #favour customer
        self.assertEqual(checkout_solution.checkout('ZYXZ'), 62) #favour customer

    def test_illegal_input(self):
        self.assertEqual(checkout_solution.checkout('a'), -1)
        self.assertEqual(checkout_solution.checkout('-'), -1)
        self.assertEqual(checkout_solution.checkout('ABCa'), -1)





