#from fractions import gcd   # Py2
from math import gcd   # Py3

class Frac:
    """Klasa reprezentująca ułamek."""

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError("Mianownik nie może być 0")
        if y < 0:
            x = -x
            y = -y
        if x == 0:
            self.x = 0
            self.y = 1
        else:
            g = gcd(x, y)      # skracanie ułamka
            self.x = x // g
            self.y = y // g

    # zwraca "x/y" lub "x" dla y=1
    def __str__(self):
        if self.y == 1:
            return str(self.x)
        return f"{self.x}/{self.y}"

    # zwraca "Frac(x, y)"
    def __repr__(self):
        return f"Frac({self.x}, {self.y})"

    # porównania
    def __eq__(self, other):
        return self.x * other.y == self.y * other.x

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return self.x * other.y < self.y * other.x

    def __le__(self, other):
        return self.x * other.y <= self.y * other.x

    # opcjonalnie, jeśli chcesz też > i >=:
    def __gt__(self, other):
        return self.x * other.y > self.y * other.x

    def __ge__(self, other):
        return self.x * other.y >= self.y * other.x

    # frac1 + frac2
    def __add__(self, other):
        x = self.x * other.y + self.y * other.x
        y = self.y * other.y
        return Frac(x, y)

    # frac1 - frac2
    def __sub__(self, other):
        x = self.x * other.y - self.y * other.x
        y = self.y * other.y
        return Frac(x, y)

    # frac1 * frac2
    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Frac(x, y)

    # frac1 / frac2, Py2
    def __div__(self, other): pass

    # frac1 / frac2, Py3
    def __truediv__(self, other):
        if other.x == 0:
            raise ZeroDivisionError("Dzielenie przez 0")
        return Frac(self.x * other.y, self.y * other.x)

    # frac1 // frac2, opcjonalnie – zwraca int
    def __floordiv__(self, other):
        num = self.x * other.y
        den = self.y * other.x
        if den < 0:
            num = -num
            den = -den
        return num // den

    # frac1 % frac2, opcjonalnie – zwraca Frac
    def __mod__(self, other):
        # a % b = a - (a // b) * b
        q = self // other           # int
        return self - Frac(q, 1) * other

    # operatory jednoargumentowe
    def __pos__(self):  # +frac = (+1)*frac
        return self

    def __neg__(self):  # -frac = (-1)*frac
        return Frac(-self.x, self.y)

    def __invert__(self):  # odwrotność: ~frac
        return Frac(self.y, self.x)

    # float(frac)
    def __float__(self):
        return self.x / self.y

    def __hash__(self):
        return hash(float(self))   # immutable fracs
        # w Pythonie set([2]) == set([2.0])
        # chcemy set([2]) == set([Frac(2)])