

class Vector:

    def __init__(self, *args):
        if len(args) == 1:
            arg = args[0]
            l = len(arg)
            row = False
            if l == 1:
                row = True
                l = len(arg[0])
            self.shape = row and (1, l) or (l, 1)
            self.values = arg
            pass
        else:
            raise AttributeError("Bad argument.")

# (1, 2, 3) * (4, 5, 6) = 1*4 + 2*5 + 3*6
    def dot(self, other):
        if self.shape == other.shape:
            res = 0
            if self.shape[0] == 1:
                for val1, val2 in zip(self.values[0], other.values[0]):
                    res += val1 * val2
            else:
                for val1, val2 in zip(self.values, other.values):
                    res += val1[0] * val2[0]
            return res
        else:
            raise AttributeError("Vectors have different shapes.")

    def T(self):
        lol = []
        if self.shape[0] == 1:
            for val in self.values[0]:
                l = []
                l.append(val)
                lol.append(l)
        else:
            l = []
            for val in self.values:
                l.append(val[0])
            lol.append(l)
        return Vector(lol)

    def __str__(self):
        return 'Vector with shape {s} and values {v}'.format(s=self.shape, v=self.values)

    def __repr__(self):
        return 'The Vector class stores the vector values and its shape, and allows to do some arithmetic operations'

    def __add__(self, other):
        if self.shape == other.shape:
            lol = []
            if self.shape[0] == 1:
                l = []
                for val1, val2 in zip(self.values[0], other.values[0]):
                    l.append(val1 + val2)
                lol.append(l)
            else:
                for val1, val2 in zip(self.values, other.values):
                    l = []
                    l.append(val1[0] + val2[0])
                    lol.append(l)
            return Vector(lol)
        else:
            raise AttributeError("Vectors have different shapes.")

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if self.shape == other.shape:
            lol = []
            if self.shape[0] == 1:
                l = []
                for val1, val2 in zip(self.values[0], other.values[0]):
                    l.append(val1 - val2)
                lol.append(l)
            else:
                for val1, val2 in zip(self.values, other.values):
                    l = []
                    l.append(val1[0] - val2[0])
                    lol.append(l)
            return Vector(lol)
        else:
            raise AttributeError("Vectors have different shapes.")

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            lol = []
            if self.shape[0] == 1:
                l = []
                for val in self.values[0]:
                    l.append(val * other)
                lol.append(l)
            else:
                for val in self.values:
                    l = []
                    l.append(val[0] * other)
                    lol.append(l)
            return Vector(lol)
        else:
            raise AttributeError("Argument is not int or float")

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            lol = []
            if self.shape[0] == 1:
                l = []
                for val in self.values[0]:
                    l.append(val / other)
                lol.append(l)
            else:
                for val in self.values:
                    l = []
                    l.append(val[0] / other)
                    lol.append(l)
            return Vector(lol)
        else:
            raise AttributeError("Argument is not int or float")

    def __rtruediv__(self, other):
        return self.__truediv__(other)
