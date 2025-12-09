from points import Point


class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)

        if self._are_collinear(self.pt1, self.pt2, self.pt3):
            raise ValueError("Punkty trójkąta są współliniowe.")


    @classmethod
    def from_points(cls, points):
        """Tworzy trójkąt z trzech obiektów Point."""
        pts = tuple(points)
        if len(pts) != 3:
            raise ValueError("Dokładnie trzy punkty są wymagane.")
        p1, p2, p3 = pts
        if not all(isinstance(p, Point) for p in (p1, p2, p3)):
            raise ValueError("Wszystkie elementy muszą być typu Point.")
        return cls(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y)

    @staticmethod
    def _are_collinear(a, b, c):
        """Zwraca True, jeśli punkty są współliniowe."""
        v1 = b - a
        v2 = c - a
        return v1.cross(v2) == 0

    def __str__(self):         # "[(x1, y1), (x2, y2), (x3, y3)]"
        # korzystamy z Point.__str__ -> "(x, y)"
        return f"[{self.pt1}, {self.pt2}, {self.pt3}]"

    def __repr__(self):        # "Triangle(x1, y1, x2, y2, x3, y3)"
        return (
            f"Triangle({self.pt1.x}, {self.pt1.y}, "
            f"{self.pt2.x}, {self.pt2.y}, "
            f"{self.pt3.x}, {self.pt3.y})"
        )

    def __eq__(self, other):   # obsługa tr1 == tr2

        if not isinstance(other, Triangle):
            return NotImplemented


        self_vertices = sorted(
            [(self.pt1.x, self.pt1.y),
             (self.pt2.x, self.pt2.y),
             (self.pt3.x, self.pt3.y)]
        )
        other_vertices = sorted(
            [(other.pt1.x, other.pt1.y),
             (other.pt2.x, other.pt2.y),
             (other.pt3.x, other.pt3.y)]
        )
        return self_vertices == other_vertices

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):
        cx = (self.pt1.x + self.pt2.x + self.pt3.x) / 3
        cy = (self.pt1.y + self.pt2.y + self.pt3.y) / 3
        return Point(cx, cy)

    def area(self):
        # |(pt2-pt1) x (pt3-pt1)| / 2
        v1 = self.pt2 - self.pt1
        v2 = self.pt3 - self.pt1
        return abs(v1.cross(v2)) / 2

    def move(self, x, y):      # przesunięcie o (x, y)
        shift = Point(x, y)
        self.pt1 = self.pt1 + shift
        self.pt2 = self.pt2 + shift
        self.pt3 = self.pt3 + shift

    def make4(self):
        #     A       po podziale    A
        #    / \                    / \
        #   /   \                  +---+
        #  /     \                / \ / \
        # C-------B              C---+---B
        A = self.pt1
        B = self.pt2
        C = self.pt3

        # środki boków
        m_ab = Point((A.x + B.x) / 2, (A.y + B.y) / 2)
        m_bc = Point((B.x + C.x) / 2, (B.y + C.y) / 2)
        m_ca = Point((A.x + C.x) / 2, (A.y + C.y) / 2)

        # trzy trójkąty przy wierzchołkach + jeden środkowy
        t1 = Triangle(A.x,   A.y,   m_ab.x, m_ab.y, m_ca.x, m_ca.y)
        t2 = Triangle(B.x,   B.y,   m_ab.x, m_ab.y, m_bc.x, m_bc.y)
        t3 = Triangle(C.x,   C.y,   m_ca.x, m_ca.y, m_bc.x, m_bc.y)
        t4 = Triangle(m_ab.x, m_ab.y, m_ca.x, m_ca.y, m_bc.x, m_bc.y)

        return (t1, t2, t3, t4)


    @property
    def top(self):
        return max(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def left(self):
        return min(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def bottom(self):
        return min(self.pt1.y, self.pt2.y, self.pt3.y)

    @property
    def right(self):
        return max(self.pt1.x, self.pt2.x, self.pt3.x)

    @property
    def width(self):
        return self.right - self.left

    @property
    def height(self):
        return self.top - self.bottom

    @property
    def topleft(self):
        return Point(self.left, self.top)

    @property
    def bottomleft(self):
        return Point(self.left, self.bottom)

    @property
    def topright(self):
        return Point(self.right, self.top)

    @property
    def bottomright(self):
        return Point(self.right, self.bottom)