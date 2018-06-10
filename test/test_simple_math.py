from algorithms.simple_math import SimpleMath

import unittest


class TestSimpleMath(unittest.TestCase):

    def test_trivial(self):
        self.assertTrue(True)

    def test_simple_sum(self):
        simple_math = SimpleMath(1, 3)
        sum_value = simple_math.sum()
        self.assertEqual(sum_value, 4)


if __name__ == '__main__':
    unittest.main()