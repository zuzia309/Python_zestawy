import itertools
import random

# (a) 0, 1, 0, 1, 0, 1, ...
def iterator_a():
    pattern = [0, 1]
    return itertools.cycle(pattern)


# (b) losowe wybieranie kierunku
def iterator_b():
    directions = ("N", "E", "S", "W")   # tuple zamiast listy
    return (random.choice(directions) for _ in itertools.count())


# (c) dni tygodnia: 0–6 powtarzane nieskonczenie
def iterator_c():
    days = list(range(7))
    return itertools.cycle(days)


# ---- TESTOWANIE ----

if __name__ == "__main__":
    print("Iterator A:")
    it_a = iterator_a()
    for _ in range(14):
        print(next(it_a), end=" ")
    print("\n")

    print("Iterator B:")
    it_b = iterator_b()
    for _ in range(14):
        print(next(it_b), end=" ")
    print("\n")

    print("Iterator C:")
    it_c = iterator_c()
    for _ in range(14):
        print(next(it_c), end=" ")
    print()