# Kod testujący moduł polys.

import unittest
from polys import Poly

def P(coeffs):
    return Poly(0).create_poly(coeffs)


class TestPoly(unittest.TestCase):

    def test_str(self):
        p = P([1, 2, 3])
        self.assertEqual(str(p), "Poly([1, 2, 3])")

    def test_add(self):
        p1 = P([1, 2])
        p2 = P([3, 4, 5])
        self.assertEqual(p1 + p2, P([4, 6, 5]))
        self.assertEqual(p1 + 5, P([6, 2]))
        self.assertEqual(5 + p1, P([6, 2]))

    def test_sub(self):
        p1 = P([1, 2])
        p2 = P([3, 4, 5])
        self.assertEqual(p1 - p2, P([-2, -2, -5]))
        self.assertEqual(p1 - 5, P([-4, 2]))
        self.assertEqual(5 - p1, P([4, -2]))

    def test_mul(self):
        p1 = P([1, 2])
        p2 = P([2, 3])
        self.assertEqual(p1 * p2, P([2, 7, 6]))
        self.assertEqual(p1 * 2, P([2, 4]))
        self.assertEqual(2 * p1, P([2, 4]))

    def test_pos(self):
        p = P([1, -2])
        self.assertEqual(+p, P([1, -2]))

    def test_neg(self):
        p = P([1, -2])
        self.assertEqual(-p, P([-1, 2]))

    def test_eq(self):
        p1 = P([1, 2])
        p2 = P([1, 2])
        self.assertEqual(p1, p2)
        # sprawdź też równość z końcowymi zerami
        p3 = P([1, 2, 0, 0])
        self.assertEqual(p1, p3)

    def test_ne(self):
        p1 = P([1, 2])
        p2 = P([1, 3])
        self.assertNotEqual(p1, p2)

    def test_eval(self):
        p = P([1, 2, 3])  # 1 + 2x + 3x^2
        self.assertEqual(p.eval(2), 17)  # 1 + 4 + 12

    def test_combine(self):
        p1 = P([1, 2])    # 1 + 2x
        p2 = P([0, 1])    # x
        # p1(p2(x)) = 1 + 2x
        self.assertEqual(p1.combine(p2), P([1, 2]))

    def test_pow(self):
        p = P([1, 1])  # 1 + x
        self.assertEqual(p ** 2, P([1, 2, 1]))  # (1 + x)^2

    def test_diff(self):
        p = P([1, 2, 3])  # 1 + 2x + 3x^2
        # pochodna: 2 + 6x
        self.assertEqual(p.diff(), P([2, 6]))

    def test_integrate(self):
        p = P([1, 4])  # 1 + 4x
        # całka: 0 + 1x + 2x^2
        self.assertEqual(p.integrate(), P([0, 1, 2]))

    def test_is_zero(self):
        p1 = P([0, 0, 0])
        p2 = P([0, 0, 1])
        self.assertTrue(p1.is_zero())
        self.assertFalse(p2.is_zero())

    def test_call_number_and_poly(self):
        p1 = P([1, 2, 3])  # 1 + 2x + 3x^2
        self.assertEqual(p1(2), 17)   # jak eval

        p2 = P([0, 1])     # x
        # p1(p2(x)) = p1(x) = 1 + 2x + 3x^2
        self.assertEqual(p1(p2), P([1, 2, 3]))

    def test_container_operations(self):
        p = P([1, 2, 3])
        self.assertEqual(len(p), 3)
        self.assertEqual(p[1], 2)
        p[2] = 7
        self.assertEqual(p[2], 7)
        self.assertEqual(p, P([1, 2, 7]))

        self.assertEqual(p[10], 0)

    def test_iter(self):
        p = P([1, 2, 3])
        coeffs = [coef for coef in p]
        self.assertEqual(coeffs, [1, 2, 3])

    def test_exceptions(self):
        with self.assertRaises(ValueError):
            Poly("string", 2)
        with self.assertRaises(ValueError):
            Poly(2, -3)
        p = P([1, 2, 3])
        with self.assertRaises(ValueError):
            p["string"] = 4
        with self.assertRaises(ValueError):
            p.eval("x")
        with self.assertRaises(ValueError):
            p.combine(123)
        with self.assertRaises(ValueError):
            p({})

if __name__ == '__main__':
    unittest.main()