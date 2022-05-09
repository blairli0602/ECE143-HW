from collections import Counter
from collections import defaultdict
import math

class Polynomial(object):

    """
    Implement a class of Polynomial object
    :a: integer
    :b: integer
    """
    def __init__(self, dic):
        assert isinstance(dic, dict)

        for i,j in dic.items():
            assert isinstance(i, int)
            assert isinstance(j,int)

        self.a = list(dic.keys())
        self.b = list(dic.values())
        self.dic = dic

    def __repr__(self):

        result = ''
        dic = dict(sorted(self.dic.items()))
        power = list(dic.keys())
        coe = list(dic.values())
        self.degree = max(dic.keys())

        if len(power) == len(coe):
            for i1, j1 in dic.items():
                if i1 == 0 and j1 == 0:
                    return str(0)

        for i in range(len(power)):

            if power[i] == 0:
                result += (str(coe[i]))

            elif coe[i] == 0:
                pass
            elif coe[i] == 1 and power[i] != 1:
                if result == '':
                    result += ' x^(' + str(power[i]) + ')'
                else:
                    result += ' + x^ (' + str(power[i]) + ')'
            elif coe[i] == 1 and power[i] == 1:
                if result == '':
                    result += ' x '
                else:
                    result += ' + x '
            elif power[i] == 1:
                if result == '':
                    result += str(coe[i]) + ' x'
                else:
                    result += ' + ' + str(coe[i]) + ' x'
            else:
                if result == '':
                    result += str(coe[i]) + ' x^(' + str(power[i]) + ')'
                else:
                    result += ' + ' + str(coe[i]) + ' x^(' + str(power[i]) + ')'

        return str(result)

    def __eq__(self, other):

        if isinstance(other, int) and isinstance(self,Polynomial):
            if other == 0:
                for i in self.b:
                    if i == 0:
                        continue
                    else:
                        return False
                return True
            else:
                return False

        elif isinstance((self,other),int):
            if self == other:
                return True
            else:
                return False
        elif isinstance(other, Polynomial):
            if sorted(self.a) == sorted(other.a) and sorted(self.b) == sorted(other.b):
                return True
            else:
                return False

    def __mul__(self, other):

        if isinstance(other,int):
            coe = self.b
            coe = [i * other for i in coe]
            power = self.a
            dic = dict(zip(power,coe))

            return Polynomial(dic)

        if isinstance(other,Polynomial):
            new_coe = defaultdict(int)
            for i1, j1 in self.dic.items():
                for i2, j2 in other.dic.items():
                    power = i1 + i2
                    coe = j1 * j2
                    new_coe[power] += coe

            result = dict(sorted(new_coe.items()))

            return Polynomial(result)

    def __rmul__(self, other):
        if isinstance(other, int):
            return self.__mul__(other)

    def __add__(self,other):

        if isinstance(other, Polynomial):
            dict1 = Counter(self.dic)
            dict2 = Counter(other.dic)

            dict1.update(dict2)
            return Polynomial(dict1)

        elif isinstance(other,int):
            coe = self.b
            power = self.a

            coe[0] = coe[0] + other
            dic = dict(zip(power, coe))

            return Polynomial(dic)

    def __radd__(self, other):
        if isinstance(other, (Polynomial, int)):
            return self.__add__(other)
        else:
            raise NotImplementedError

    def __sub__(self, other):
        if self == other:
            dic = {0: 0}
            return Polynomial(dic)
        if isinstance(other, Polynomial):
            dict1 = Counter(self.dic)
            dict2 = Counter(other.dic)

            dict1.subtract(dict2)
            return Polynomial(dict1)

        elif isinstance(other, int):
            coe = self.b
            power = self.a

            coe[0] = coe[0] - other
            dic = dict(zip(power, coe))

            return Polynomial(dic)

    def __rsub__(self, other):
        if isinstance(other, (int,Polynomial)):
            return self.__sub__(other)

    def __truediv__(self,other):

        if isinstance(other, Polynomial):

            dic = self._long_div(self,other)
            return dic

        elif isinstance(other, int):
            coe = self.b
            power = self.a

            coe = [i/other for i in coe]
            dic = dict(zip(power,coe))

            return Polynomial(dic)

        else:
            raise NotImplementedError

    def __rtruediv__(self, other):
        if isinstance(other, Polynomial):
            return self.__truediv__(other, self)

        elif isinstance(other, (int, float)):
            raise NotImplementedError
        else:
            raise NotImplementedError


    @staticmethod
    def _long_div(p1, p2):

        ans = defaultdict(int)

        while p1 != 0  :
            if p1._degree() < p2._degree():
                raise NotImplementedError
            else:
                degree1 = p1._degree()
                degree2 = p2._degree()

                pow1 = p1.a
                pow2 = p2.a

                coe1 = p1.b
                coe2 = p2.b

                dic1 = p1.dic
                dic2 = p2.dic

                shift = degree1 - degree2
                if dic1[degree1] % dic2[degree2] == 0:
                    shiftcoe = int(dic1[degree1] / dic2[degree2])
                    ans[shift] = shiftcoe
                else:
                    raise NotImplementedError

                newpow2 = [(i + shift) for i in pow2]
                newp2 = dict(zip(newpow2, coe2))

                p1 = p1 - shiftcoe*Polynomial(newp2)

        return Polynomial(ans)

    def _degree(self):
        if isinstance(self, Polynomial):
            dic = self.dic
            dic1 = dic.copy()
            for k,v in dic1.items():
                if v == 0:
                    del dic[k]
            result_dic = list(dic.keys())
        elif isinstance(self,list):
            result_dic = self
        return max(result_dic)

    def subs(self, x):
        assert isinstance(x,int)

        result = 0
        for i, j in self.dic.items():
            result += (j * pow(x,i))
        return result


p = Polynomial({0: 8, 1: 2, 3: 4})  # keys are powers, values are coefficients
q = Polynomial({0: 8, 1: 2, 2: 8, 4: 4})

print("Exact repr output not important, the values are the point of the exercise\n")

print("Actual | expected ")
print("---------------------------")
print(repr(p), "| 8 + 2 x + 4 x^(3)")
print(p * 3, "| 24 + 6x + 12x^(3)")
print(3 * p, "| 24 + 6x + 12x^(3)")  # multiplication is commutative!
print(p + q, "| 16 + 4x + 8x^(2) + 4x ^ (3) + 4x ^ (4)")  # add two polynomials
print(p * 4 + 5 - 3 * p - 1, "| 12 + 2x + 4x ^ (3)")  # compose operations and add/subtract constants
print(type(p - p), "| Polynomial")  # zero requires special handling but is still a Polynomial
print(p * q,
      "| 64 + 32x + 68x ^ (2) + 48x ^ (3) + 40x ^ (4) + 40x ^ (5) + 16x ^ (7)")  # polynomial by polynomial multiplication works as usual
print(p.subs(10), "| 4028")  # substitute in integers and evaluate
print((p - p) == 0, "| True")
print(p == q, "| False")
p = Polynomial({0: 8, 1: 0, 3: 4})  # keys are powers, values are coefficients
print(repr(p), '| 8 + 4 x^(3)')

# Division

print(Polynomial({2: 1, 0: -1}) / Polynomial({1: 1, 0: -1}), "| 1 + x")
print(Polynomial({2: 1, 0: -4}) / Polynomial({1: 1, 0: -2}), "| 2 + x")
print(Polynomial({2: 1, 0: -9}) / Polynomial({1: 1, 0: 3}))

# long division tests, cause this part was tricky
a = Polynomial({0: 1, 1: 4, 2: 1})
b = Polynomial({1: 2})
c = Polynomial({0: 5, 2: 3})

product = a * b * c

assert product / c == a * b
assert product / b == a * c
assert product / a == b * c
assert product / (a * b) == c
assert product / (b * c) == a

try:
    print(p / Polynomial({1: 1, 0: -3}))  # raises NotImplementedError"""
    raise AssertionError("failed to raise proper error")
except NotImplementedError:
    pass

print("\nLong division tests passed")

