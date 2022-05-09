class Interval(object):
    def __init__(self, a, b):
        """
        :a: integer
        :b: integer
        """
        assert a < b
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __repr__(self):
        return 'Interval({},{})'.format(self._a, self._b)

    def __eq__(self, other):
        if self._a == other._a and self._b ==other._b:
            return True
        else:
            return False

    def __lt__(self, other): #(1,2) (3,4)
        if self._b <= other._a:
            return True
        else:
            return False

    def __le__(self, other):#(2,5) (1,6)
        if self._a <= other._a and other._a < self._b <= other._b:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.a >= other._b:
            return True
        else:
            return False

    def __ge__(self, other): #(5,9) (3,8)
        if self._a > other._a and self._a < other._b <=self._b:
            return True
        else:
            return False

    def __contains__(self, other):
        if self._a <= other._a < other._b <= self._b:
            return True
        else:
            return False

    def __add__(self, other):
        if self == other:
            return self
        elif self in other:
            return other
        elif other in self:
            return self
        elif self < other:
            return [self, other]
        elif other < self:
            return [other,self]
        elif self <= other:
            return self.__class__(self._a,other._b)
        elif self >= other:
            return self.__class__(other._a,self._b)
