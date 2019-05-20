class SimpleMath(object):

    """
    A simple class to do math operations

    Attributes
        x: The first float number
        y: The second float number
    """

    x = 0.0
    y = 0.0

    def __init__(self, x = 0.0, y = 0.0):
        self.x = x
        self.y = y

    def sum(self):
        return self.x + self.y

    def substract(self):
        return self.x - self.y