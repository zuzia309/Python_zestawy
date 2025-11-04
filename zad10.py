"""
Stworzyć słownik tłumaczący liczby zapisane w systemie rzymskim (z literami I, V, X, L, C, D, M) na liczby arabskie
(podać kilka sposobów tworzenia takiego słownika). Mile widziany kod tłumaczący całą liczbę [funkcja roman2int()].
"""

def roman_to_int(roman_str):
    roman_map = {
        'I': 1, 'V': 5, 'X': 10,
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    for symbol in roman_str:
        if symbol not in roman_map:
            print(f"'{symbol}' nie jest poprawnym znakiem w systemie rzymskim!")
            return None

    total = 0
    last_value = 0

    for symbol in reversed(roman_str):
        current = roman_map[symbol]
        if current < last_value:
            total -= current
        else:
            total += current
        last_value = current

    return total

roman_input = input("Podaj liczbe rzymska: ")
arabic_value = roman_to_int(roman_input)

if arabic_value is not None:
    print(f"Liczba arabska to: {arabic_value}")