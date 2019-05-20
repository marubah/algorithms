from algorithms.inversion import Inversion

import unittest

from algorithms.quick_sort import QuickSort, pivot_first, pivot_last, pivot_median


class TestQuickSort(unittest.TestCase):

    def test_trivial(self):
        self.assertTrue(True)


    def test_quick_sort_small_array_first_pivot(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([3, 4, 2, 5, 1], pivot_first)
        self.assertEqual(cant_comparisons, 6)

    def test_quick_sort_small_array_first_pivot_worst_case(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([1, 2, 3, 4, 5], pivot_first)
        self.assertEqual(cant_comparisons, 10)

    def test_quick_sort_small_array_last_pivot(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([3, 4, 2, 5, 1], pivot_last)
        self.assertEqual(cant_comparisons, 8)

    def test_quick_sort_small_array_last_pivot_worst_case(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([2, 3, 4, 5, 1], pivot_last)
        self.assertEqual(cant_comparisons, 10)

    def test_quick_sort_small_odd_array_median_pivot(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([3, 4, 2, 5, 1], pivot_median)
        self.assertEqual(cant_comparisons, 6)

    def test_quick_sort_small_odd_array_median_pivot_sorted(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([1, 2, 3, 4, 5], pivot_median)
        self.assertEqual(cant_comparisons, 6)

    def test_quick_sort_small_even_array_median_pivot(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([6, 3, 1, 5, 2, 4], pivot_median)
        self.assertEqual(cant_comparisons, 8)

    def test_quick_sort_small_even_array_median_pivot_right(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([6, 4, 3, 5, 2, 1], pivot_median)
        self.assertEqual(cant_comparisons, 8)

    def test_quick_sort_medium_even_array_median_pivot(self):
        quick_sort_obj = QuickSort()
        cant_comparisons = quick_sort_obj.quick_sort([8, 1, 9, 4, 3, 2, 0, 6, 5, 7], pivot_median)
        self.assertEqual(cant_comparisons, 22)

    def test_quick_sort_long_array_first_pivot(self):
        quick_sort_obj = QuickSort()
        text_file = open("data_quick_sort.txt", "r")
        array = text_file.readlines()
        array = [int(x.strip()) for x in array]
        text_file.close()
        cant_comparisons = quick_sort_obj.quick_sort(array, pivot_first)
        self.assertEqual(cant_comparisons, 0)

    def test_quick_sort_long_array_last_pivot(self):
        quick_sort_obj = QuickSort()
        text_file = open("data_quick_sort.txt", "r")
        array = text_file.readlines()
        array = [int(x.strip()) for x in array]
        text_file.close()
        cant_comparisons = quick_sort_obj.quick_sort(array, pivot_last)
        self.assertEqual(cant_comparisons, 1)

    def test_quick_sort_long_array_median_pivot(self):
        quick_sort_obj = QuickSort()
        text_file = open("data_quick_sort.txt", "r")
        array = text_file.readlines()
        array = [int(x.strip()) for x in array]
        text_file.close()
        cant_comparisons = quick_sort_obj.quick_sort(array, pivot_median)
        self.assertEqual(cant_comparisons, 2)


if __name__ == '__main__':
    unittest.main()
