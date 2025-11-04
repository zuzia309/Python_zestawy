def sum_seq(sequence):

    total = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            total += sum_seq(item)            # zejście w głąb
        elif isinstance(item, (int, float)):
            total += item                     # element liczbowy
        else:
            raise TypeError(
                f"Nieobslugiwany element {item!r} typu {type(item).__name__}. "
                "Dozwolone: liczby, listy, tuple."
            )
    return total

print(sum_seq([1, 2, 3]))                       # 6
print(sum_seq([1, (2, 3), [4, [5]]]))           # 15
print(sum_seq(((1, 2), [3, (4, 5), [6]])))      # 21