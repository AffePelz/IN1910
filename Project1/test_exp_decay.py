import unittest
from exp_decay import ExponentialDecay


class TestExponentialDecay(unittest.TestCase):
    def test_ExponentialDecay(self):
        expected = -1.28
        test_value = ExponentialDecay(0.4)
        calculated = test_value(99, 3.2)
        self.assertAlmostEqual(expected, calculated)


if __name__ == '__main__':
    unittest.main()
