import math
import numpy as np


def pivot_first(array, left_boundary, right_boundary):
    pivot = left_boundary
    return pivot


def pivot_last(array, left_boundary, right_boundary):
    pivot = right_boundary
    return pivot


def pivot_median(array, left_boundary, right_boundary):
    middle = (right_boundary - left_boundary)//2 + left_boundary

    if ((array[left_boundary] > array[right_boundary] and array[left_boundary] < array[middle]) or
        (array[left_boundary] > array[middle] and array[left_boundary] < array[right_boundary])):
        return left_boundary
    elif ((array[right_boundary] > array[left_boundary] and array[right_boundary] < array[middle]) or
        (array[right_boundary] > array[middle] and array[right_boundary] < array[left_boundary])):
        return right_boundary
    else:
        return middle


class QuickSort(object):
    """
        A class to order arrays with QuickSort and count the number of comparisons needed

        Attributes
            array: input array to be ordered
    """

    def quick_sort(self, array, choose_pivot = pivot_first):
        return self.__quick_sort_rec(array, 0, len(array)-1, 0, choose_pivot)

    def __quick_sort_rec(self, array, left_boundary, right_boundary, number_comparisons, choose_pivot):

        if right_boundary - left_boundary <= 1:
            if right_boundary - left_boundary == 0:
                pass
            else:
                number_comparisons += 1
                if array[left_boundary] > array[right_boundary]:
                    (array[right_boundary],array[left_boundary]) = (array[left_boundary],array[right_boundary])
                else:
                    pass
            return number_comparisons
        else:
            pass

        number_comparisons += right_boundary - left_boundary

        p = choose_pivot(array, left_boundary, right_boundary)

        #swap pivot to the first element of the subarray
        (array[left_boundary], array[p]) = (array[p], array[left_boundary])

        div = self.partition(array, left_boundary, right_boundary)

        if div > left_boundary:
            number_comparisons = self.__quick_sort_rec(array, left_boundary, div - 1, number_comparisons, choose_pivot)
        if div < right_boundary:
            number_comparisons = self.__quick_sort_rec(array, div + 1, right_boundary, number_comparisons, choose_pivot)

        return number_comparisons

    def partition(self, array, left_boundary, right_boundary):
        pivot = array[left_boundary]
        i = left_boundary + 1

        for j in range(left_boundary + 1 , right_boundary+1):
            if array[j] < pivot:
                (array[j],array[i]) = (array[i],array[j])
                i += 1
            else:
                pass

        (array[left_boundary], array[i-1]) = (array[i-1], array[left_boundary])

        return i-1
