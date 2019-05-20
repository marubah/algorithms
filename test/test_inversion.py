from algorithms.inversion import Inversion

import unittest


class TestInversion(unittest.TestCase):

    def test_trivial(self):
        self.assertTrue(True)

    def test_inversion_even(self):
        inversion_obj = Inversion()
        cant_inversions = inversion_obj.inversion([6, 5, 4, 3, 2, 1])
        self.assertEqual(cant_inversions, 15)

    def test_inversion_odd(self):
        inversion_obj = Inversion()
        cant_inversions = inversion_obj.inversion([9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(cant_inversions, 36)

    def test_inversion_rdm(self):
        inversion_obj = Inversion()
        cant_inversions = inversion_obj.inversion([1, 3, 5, 2, 4, 6])
        self.assertEqual(cant_inversions, 3)

    def test_inversion_long_array(self):
        inversion_obj = Inversion()
        text_file = open("data.txt", "r")
        array = text_file.readlines()
        array = [int(x.strip()) for x in array]
        text_file.close()
        cant_inversions = inversion_obj.inversion(array)
        self.assertEqual(cant_inversions, 0)


if __name__ == '__main__':
    unittest.main()
