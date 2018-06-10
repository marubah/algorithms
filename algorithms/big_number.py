class BigNumber(object):

    """
    A class to manage math with big numbers

    Attributes
        x: The first float number
        y: The second float number
    """

    x = ""
    y = ""

    def __init__(self, x = "", y = ""):
        self.x = x
        self.y = y

    def multiplication(self, x = "", y = ""):

        if len(x) == 1 or len(y) == 1:
            return int(x) * int(y)
        else:
            if len(x) % 2 == 0:
                x_left = x[:int(len(x) / 2)]
                x_right = x[int(len(x) / 2):]
            else:
                x_left = x[:int(len(x) / 2)+1]
                x_right = x[int(len(x) / 2)+1:]

            if len(y) % 2 == 0:
                y_left = y[:int(len(y) / 2)]
                y_right = y[int(len(y) / 2):]
            else:
                y_left = y[:int(len(y) / 2)+1]
                y_right = y[int(len(y) / 2)+1:]

            multiplication_left = self.multiplication(x_left,y_left)
            multiplication_right = self.multiplication(x_right, y_right)
            sum_x = int(x_left) + int(x_right)
            sum_y = int(y_left) + int(y_right)
            multiplication_sum_x_y = self.multiplication(str(sum_x),str(sum_y))
            sum_multiplications = int(multiplication_sum_x_y) - int(multiplication_left) - int(multiplication_right)
            zeros = int(len(x) / 2)
            new_multiplication_left = str(multiplication_left) + (zeros * 2) * "0"
            new_sum_multiplications = str(sum_multiplications) + zeros * "0"
            result = int(new_multiplication_left) + int(multiplication_right) + int(new_sum_multiplications)
            return result
