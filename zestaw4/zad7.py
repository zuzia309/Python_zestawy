def flatten(sequence):
    flat = []
    for item in sequence:
        if isinstance(item, (list, tuple)):
            flat.extend(flatten(item))   # rekurencyjne spłaszczanie
        else:
            flat.append(item)
    return flat

sequence = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(sequence))