def factorial_iter(n):
    if n < 0:
        raise ValueError("Silnia nie jest zdefiniowana dla liczb ujemnych")

    wynik = 1
    for liczba in range(1, n + 1):
        wynik *= liczba
    return wynik


print(f"6! = {factorial_iter(6)}")