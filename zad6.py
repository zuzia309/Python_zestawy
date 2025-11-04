"""
Napisać program rysujący prostokąt zbudowany z małych kratek. Należy zbudować pełny string,
 a potem go wypisać. Przykładowy prostokąt składający się 2x4 pól ma postać:

+---+---+---+---+
|   |   |   |   |
+---+---+---+---+
|   |   |   |   |
+---+---+---+---+

"""
dl = int(input("Podaj długość: "))
wys = int(input("Podaj wysokość: "))

if dl <= 0 or wys <= 0:
    print("Wartości nie mogą być <= 0")
else:
    for n in range(1, wys + 1):
        print("+" + "---+" * dl)
        print("|" + "   |" * dl)

    print("+" + "---+" * dl)