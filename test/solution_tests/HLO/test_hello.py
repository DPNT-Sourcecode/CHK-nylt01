from solutions.HLO import hello_solution
import unittest


class TestHLO(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello_solution.hello('John'), 'Hello, John!')
