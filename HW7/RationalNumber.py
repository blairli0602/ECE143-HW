import math

class Rational(object):

    """
    Implement a class of rational numbers
    :a: integer
    :b: integer
    """

    def __init__(self, a, b):
        assert isinstance(a, int)
        assert isinstance(b, int)
        self._a = a
        self._b = b

    def __eq__(self, other):
        if float(self) == float(other):
            return True
        return False

    def __ge__(self,other):
        if float(self) >= float(other):
            return True
        return False

    def __le__(self, other):
        if float(self) <= float(other):
            return True
        return False

    def __gt__(self, other):
        if float(self) > float(other):
            return True

    def __lt__(self, other):
        if float(self) < float(other):
            return True
        return False

    def __repr__(self):
        if  self._a//self._b == self._a/self._b:
            return str(int(self._a / self._b))
        else:
            return str(self._a) + '/' + str(self._b)

    def __truediv__(self, other):
        if isinstance(other, int):
            return Rational(self._a, self._b*other)
        elif isinstance(other, Rational):
            return Rational(self._a * other._b, self._b*other._a)

    def __rtruediv__(self, other):

        if isinstance(other,int):
            return Rational(self._b*other, self._a)
        elif isinstance(other, Rational):
            return Rational( self._b * other._a,self._a * other._b)

    def __float__(self):
        return float(self._a/self._b)

    def __int__(self):
        return int(self._a/self._b)

    def __sub__(self, other):

        if isinstance(other, Rational):

            gcd = math.gcd(self._b, other._b)
            mul = int(self._b * other._b / gcd)
            mul1 = int(mul/ self._b)
            mul2 = int(mul / other._b)

            result1a = self._a * mul1
            result2a = other._a * mul2

            return Rational(result1a - result2a, mul).simple()

        elif isinstance(other, int):

           return Rational(self._a - other * self._b,self._b)

    def __add__(self, other):

        if isinstance(other, Rational):

            gcd = math.gcd(self._b, other._b)
            mul = int(self._b * other._b / gcd)
            mul1 = int(mul / self._b)
            mul2 = int(mul / other._b)

            result1a = self._a * mul1
            result2a = other._a * mul2

            return Rational(result1a + result2a, mul).simple()

        elif isinstance(other, int):

            return Rational(self._a + other * self._b, self._b)

    def __radd__(self, other):
        if isinstance(other, int):
            return self.__add__(other)

    def __pow__(self, power, modulo=None):

        return Rational(self._a ** power , self._b ** power)

    def __mul__(self, other):

        if isinstance(other, Rational):
            return Rational( self._a * other._a, self._b * other._b).simple()
        elif isinstance(other, int):
            return Rational(self._a * other, self._b)

    def __neg__(self):

        return Rational(self._a * (-1), self._b)

    def __abs__(self):

        return Rational(abs(self._a),abs(self._b))

    def simple(self):

        gcd = int(math.gcd(self._a,self._b))
        return Rational(int(self._a/gcd),int(self._b/gcd))


def square_root_rational(x,abs_tol=Rational(1,1000)):
    """
    find square roor
    :x: Rational class
    :abs_tol: Rational class

    """
    assert isinstance(x, Rational)
    assert isinstance(abs_tol, Rational)
    assert x > 0
    assert abs_tol > 0

    left = 0
    right = max(1.0,x)

    while True:

        mid = (left + right) / 2

        if abs(float(mid) - math.sqrt(x)) < abs_tol:
            return mid
        elif mid ** 2 < x:
            left = mid
        else:
            right = mid

    return mid



r = Rational(3,4)
b = Rational(1,2)

# #print(Rational(10,3) * Rational(101,8))
# print(-Rational(12345,128191) + Rational(101,103) * 30 / 44)
#
# #print(Rational(100,10))
# #print((-Rational(12345,128191)))
#
# print(sorted([Rational(10,3),Rational(9,8), Rational(10,1), Rational(1,100)]))
# #print(math.gcd(4,6))

print(square_root_rational(Rational(1112,3),abs_tol=Rational(1,1000)))

