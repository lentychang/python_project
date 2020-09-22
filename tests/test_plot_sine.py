import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) +
                "/../scripts/")

try:
    from plot_sine import fib as fib
except ImportError:
    raise

print(__file__)

class TestFib(unittest.TestCase):
    def test_positive_int(self):
        self.assertEqual(list(fib(3))[-1],2)
    def test_zero(self):
        self.assertFalse(list(fib(0)))
    def test_negitive_int(self):
        # self.assertRaises(TypeError,fib(-1))
        self.assertFalse(list(fib(-1)))
    def test_float(self):
        # Need to find another way to check float, using dynamic check?
        # self.assertRaises(TypeError,fib(1.5))
        self.assertEqual(list(fib(1.5))[-1],1)

if __name__ == '__main__':
    unittest.main()