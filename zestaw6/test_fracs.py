# test_fracs.py
import unittest
from fracs import Frac

class TestFrac(unittest.TestCase):

    def setUp(self):
        self.f1 = Frac(1, 2)
        self.f2 = Frac(3, 4)
        self.f3 = Frac(-2, 3)
        self.f4 = Frac(4, -6)

    # test __str__ i __repr__
    def test_str_repr(self):
        self.assertEqual(str(self.f1), "1/2")
        self.assertEqual(str(Frac(3, 1)), "3")
        self.assertEqual(repr(self.f1), "Frac(1, 2)")
        self.assertEqual(repr(self.f3), "Frac(-2, 3)")

    # test normalizacji i gcd
    def test_normalization(self):
        self.assertEqual(Frac(2, 4), Frac(1, 2))
        self.assertEqual(Frac(-2, -4), Frac(1, 2))
        self.assertEqual(self.f3, self.f4)
        self.assertEqual(Frac(0, 5), Frac(0, 1))

    # test porównań
    def test_cmp(self):
        self.assertTrue(Frac(1, 2) == Frac(2, 4))
        self.assertFalse(Frac(1, 2) == Frac(3, 4))
        self.assertTrue(Frac(1, 2) != Frac(3, 4))
        self.assertFalse(Frac(1, 2) != Frac(2, 4))

        self.assertTrue(Frac(1, 2) < Frac(3, 4))
        self.assertFalse(Frac(3, 4) < Frac(1, 2))

        self.assertTrue(Frac(1, 2) <= Frac(2, 4))
        self.assertTrue(Frac(1, 2) <= Frac(3, 4))
        self.assertFalse(Frac(3, 4) <= Frac(1, 2))

        self.assertTrue(Frac(3, 4) > Frac(1, 2))
        self.assertFalse(Frac(1, 2) > Frac(3, 4))

        self.assertTrue(Frac(3, 4) >= Frac(1, 2))
        self.assertTrue(Frac(1, 2) >= Frac(2, 4))
        self.assertFalse(Frac(1, 2) >= Frac(3, 4))

    # test dodawania
    def test_add(self):
        self.assertEqual(self.f1 + self.f2, Frac(5, 4))
        self.assertEqual(self.f1 + Frac(1, 2), Frac(1, 1))
        self.assertEqual(self.f3 + self.f4, Frac(-4, 3))

    # test odejmowania
    def test_sub(self):
        self.assertEqual(self.f2 - self.f1, Frac(1, 4))
        self.assertEqual(self.f1 - self.f1, Frac(0, 1))
        self.assertEqual(self.f3 - self.f4, Frac(0, 1))

    # test mnożenia
    def test_mul(self):
        self.assertEqual(self.f1 * self.f2, Frac(3, 8))
        self.assertEqual(self.f1 * Frac(2, 1), Frac(1, 1))
        self.assertEqual(self.f3 * self.f4, Frac(4, 9))

    # test dzielenia
    def test_truediv(self):
        self.assertEqual(self.f2 / self.f1, Frac(3, 2))
        self.assertEqual(self.f1 / self.f2, Frac(2, 3))
        with self.assertRaises(ZeroDivisionError):
            self.f1 / Frac(0, 1)

    # test dzielenia całkowitego i reszty
    def test_floor_mod(self):
        self.assertEqual(Frac(7, 3) // Frac(1, 2), 4)
        a = Frac(7, 3)
        b = Frac(1, 2)
        q = a // b
        r = a % b
        self.assertEqual(a, Frac(q, 1) * b + r)

    # test operatorów jednoargumentowych
    def test_unary(self):
        self.assertEqual(+self.f1, self.f1)
        self.assertEqual(-self.f1, Frac(-1, 2))
        self.assertEqual(~self.f1, Frac(2, 1))

    # test float()
    def test_float(self):
        self.assertAlmostEqual(float(Frac(1, 2)), 0.5)
        self.assertAlmostEqual(float(Frac(2, 4)), 0.5)
        self.assertAlmostEqual(float(Frac(-1, 4)), -0.25)

    # test błędów w konstruktorze
    def test_constructor_errors(self):
        with self.assertRaises(ValueError):
            Frac(1, 0)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()