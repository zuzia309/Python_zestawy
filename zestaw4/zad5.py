def odwracanie_iter(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1


def odwracanie_rek(L, left, right):
    if left >= right:
        return
    L[left], L[right] = L[right], L[left]
    odwracanie_rek(L, left + 1, right - 1)


# Test
L1 = [10, 20, 30, 40, 50, 60]
L2 = [10, 20, 30, 40, 50, 60]

odwracanie_iter(L1, 1, 4)
odwracanie_rek(L2, 1, 4)

print("Iteracyjnie:", L1)
print("Rekurencyjnie:", L2)