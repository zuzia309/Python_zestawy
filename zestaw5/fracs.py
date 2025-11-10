from math import gcd


def simplify(frac):
    """Upraszcza ułamek, przenosząc znak do licznika i skracając przez NWD."""
    num, den = frac
    if den < 0:
        num, den = -num, -den
    nwd = gcd(abs(num), abs(den))
    return [num // nwd, den // nwd]

def valid_frac(frac):
    """Sprawdza, czy ułamek jest poprawny (mianownik ≠ 0)."""
    if frac[1] == 0:
        raise ValueError("Mianownik nie może byc zerem")
    return True

def add_frac(a, b):
    a1, a2 = a
    b1, b2 = b
    num = a1 * b2 + b1 * a2
    den = a2 * b2
    return simplify([num, den])


def sub_frac(a, b):
    a1, a2 = a
    b1, b2 = b
    num = a1 * b2 - b1 * a2
    den = a2 * b2
    return simplify([num, den])


def mul_frac(a, b):
    a1, a2 = a
    b1, b2 = b
    num = a1 * b1
    den = a2 * b2
    return simplify([num, den])


def div_frac(a, b):
    a1, a2 = a
    b1, b2 = b

    if b1 == 0:
        raise ZeroDivisionError("Dzielenie przez zero")

    num = a1 * b2
    den = a2 * b1
    return simplify([num, den])


def is_positive(frac):
    num, den = frac
    return num * den > 0


def is_zero(frac):
    num, _ = frac
    return num == 0


def cmp_frac(a, b):

    a1, a2 = a
    b1, b2 = b

    left = a1 * b2
    right = b1 * a2

    if left < right:
        return -1
    elif left > right:
        return 1
    else:
        return 0


def frac2float(frac):
    num, den = frac
    return num / den