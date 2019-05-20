import math


class Inversion(object):
    """
        A class to order big arrays and count the number of inversions needed

        Attributes
            array: input array to be ordered
    """

    array = list()

    def __init__(self, array=list()):
        self.array = array

    def inversion(self, array=list()):

        if len(array) == 1:
            cant_inversions = 0
            return cant_inversions
        elif len(array) == 2:
            if array[0] <= array[1]:
                cant_inversions = 0
            else:
                aux = array[0]
                array[0] = array[1]
                array[1] = aux
                cant_inversions = 1
            return cant_inversions
        else:
            array_left = array[0:math.ceil(len(array) / 2)]
            array_right = array[math.ceil(len(array) / 2):]

            cant_inversions_left = self.inversion(array_left)
            cant_inversions_right = self.inversion(array_right)
            cant_inversions_merge = 0
            i = 0
            j = 0

            array_ordered = list()

            for k in range(0, len(array)):
                if array_left[i] <= array_right[j]:
                    array_ordered.append(array_left[i])
                    i += 1
                    if i == len(array_left):
                        for z in range(j, len(array_right)):
                            array_ordered.append(array_right[z])
                        break
                    else:
                        pass
                else:
                    array_ordered.append(array_right[j])
                    cant_inversions_merge += len(array_left) - i
                    j += 1
                    if j == len(array_right):
                        for z in range(i, len(array_left)):
                            array_ordered.append(array_left[z])
                        break
                    else:
                        pass

            for k in range(0, len(array_ordered)):
                array[k] = array_ordered[k]

            cant_inversions = cant_inversions_merge + cant_inversions_right + cant_inversions_left

            return cant_inversions
