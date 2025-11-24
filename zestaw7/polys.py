class Poly:
    """Klasa reprezentująca wielomiany."""

    def __init__(self, c=0, n=0):
        if not isinstance(c, (int, float)):
            raise ValueError("Wspolczynnik c musi byc liczba.")
        if not isinstance(n, int) or n < 0:
            raise ValueError("Stopien n musi byc nieujemna liczba calkowita.")
        self.a = [0] * (n + 1)
        self.a[-1] = c
        self._trim()


    def _trim(self):
        while len(self.a) > 1 and self.a[-1] == 0:
            self.a.pop()
        return self

    def create_poly(self, coeffs):
        coeffs = list(coeffs)
        while len(coeffs) > 1 and coeffs[-1] == 0:
            coeffs.pop()
        obj = Poly(0)
        obj.a = coeffs
        return obj


    def __str__(self):
        return f"Poly({self.a})"

    def __repr__(self):
        return str(self)


    def __add__(self, other):
        if isinstance(other, Poly):
            size = max(len(self.a), len(other.a))
            result = [0] * size
            for i in range(size):
                c1 = self.a[i] if i < len(self.a) else 0
                c2 = other.a[i] if i < len(other.a) else 0
                result[i] = c1 + c2
            return self.create_poly(result)

        elif isinstance(other, (int, float)):
            result = self.a[:]
            result[0] += other
            return self.create_poly(result)

        raise ValueError("Dodawac mozna tylko Poly lub liczbe.")

    __radd__ = __add__


    def __sub__(self, other):
        if isinstance(other, Poly):
            size = max(len(self.a), len(other.a))
            result = [0] * size
            for i in range(size):
                c1 = self.a[i] if i < len(self.a) else 0
                c2 = other.a[i] if i < len(other.a) else 0
                result[i] = c1 - c2
            return self.create_poly(result)

        elif isinstance(other, (int, float)):
            result = self.a[:]
            result[0] -= other
            return self.create_poly(result)

        raise ValueError("Odejmowac mozna tylko Poly lub liczbe.")

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            result = [-c for c in self.a]
            result[0] += other
            return self.create_poly(result)
        raise ValueError("Lewym argumentem musi byc liczba.")


    def __mul__(self, other):
        if isinstance(other, Poly):
            size = len(self.a) + len(other.a) - 1
            result = [0] * size
            for i in range(len(self.a)):
                for j in range(len(other.a)):
                    result[i + j] += self.a[i] * other.a[j]
            return self.create_poly(result)

        elif isinstance(other, (int, float)):
            result = [c * other for c in self.a]
            return self.create_poly(result)

        raise ValueError("Mnozyc mozna tylko Poly lub liczbe.")

    __rmul__ = __mul__


    def __pos__(self):
        return self

    def __neg__(self):
        return self.create_poly([-c for c in self.a])


    def is_zero(self):
        return all(c == 0 for c in self.a)

    def __eq__(self, other):
        if not isinstance(other, Poly):
            return False

        a1 = self.a[:]
        a2 = other.a[:]
        while len(a1) > 1 and a1[-1] == 0:
            a1.pop()
        while len(a2) > 1 and a2[-1] == 0:
            a2.pop()

        return a1 == a2

    def __ne__(self, other):
        return not self == other


    def eval(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError("eval(x): x musi byc liczba.")
        result = 0
        for coef in reversed(self.a):
            result = result * x + coef
        return result

    def combine(self, other):
        if not isinstance(other, Poly):
            raise ValueError("combine(other): other musi byc Poly.")
        result = Poly(0)
        for coef in reversed(self.a):
            result = result * other + Poly(coef)
        return result

    def __call__(self, x):
        if isinstance(x, (int, float)):
            return self.eval(x)
        if isinstance(x, Poly):
            return self.combine(x)
        raise ValueError("Argument poly(x) musi byc liczba albo Poly.")


    def __pow__(self, n):
        if not isinstance(n, int) or n < 0:
            raise ValueError("Potega musi byc nieujemna liczba calkowita.")
        result = Poly(1)
        for _ in range(n):
            result *= self
        return result


    def diff(self):
        if len(self.a) == 1:
            return Poly(0)
        result = [i * self.a[i] for i in range(1, len(self.a))]
        return self.create_poly(result)


    def integrate(self):
        result = [0] + [self.a[i] / (i + 1) for i in range(len(self.a))]
        return self.create_poly(result)


    def __len__(self):
        return len(self.a)

    def __getitem__(self, i):
        if not isinstance(i, int) or i < 0:
            raise ValueError("Indeks musi byc nieujemny.")
        return self.a[i] if i < len(self.a) else 0

    def __setitem__(self, i, val):
        if not isinstance(i, int) or i < 0:
            raise ValueError("Indeks musi byc nieujemny.")
        if not isinstance(val, (int, float)):
            raise ValueError("Wspolczynnik musi byc liczba.")
        if i >= len(self.a):
            self.a.extend([0] * (i + 1 - len(self.a)))
        self.a[i] = val
        self._trim()

    def __iter__(self):
        return iter(self.a)