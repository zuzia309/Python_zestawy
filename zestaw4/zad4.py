def fibonacci(n):
    if n < 0:
        raise ValueError("Ciąg Fibonacciego nie jest zdefiniowany dla liczb ujemnych")

    if n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


print(f"F(0) = {fibonacci(0)}")
print(f"F(1) = {fibonacci(1)}")
print(f"F(5) = {fibonacci(5)}")
print(f"F(10) = {fibonacci(10)}")