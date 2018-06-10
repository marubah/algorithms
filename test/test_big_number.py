from algorithms.big_number import BigNumber

import unittest


class TestBigNumber(unittest.TestCase):

    def test_trivial(self):
        self.assertTrue(True)

    def test_big_number(self):
        big_number = BigNumber()
        multiplication_result = big_number.multiplication("3141592653589793238462643383279502884197169399375105820974944592", "2718281828459045235360287471352662497757247093699959574966967627")
        self.assertEqual(multiplication_result, 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184)


if __name__ == '__main__':
    unittest.main()