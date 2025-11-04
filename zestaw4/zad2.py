# zadanie 2.5

def make_ruler(length):
    marks = "|"
    numbers = "0"
    for i in range(1, length + 1):
        marks += "....|"
        numbers += f"{i:5}"

    # zamiast print – łączymy wszystko w jeden tekst
    result = marks + "\n" + numbers
    return result

#zadanie 2.6
def make_grid(rows, cols):
    if rows <= 0 or cols <= 0:
        return "Wartosci musza byc wieksze od zera"

    horizontal = "+" + "---+" * cols
    vertical = "|" + "   |" * cols
    grid = ""

    for _ in range(rows):
        grid += horizontal + "\n" + vertical + "\n"
    grid += horizontal  # ostatnia dolna linia

    return grid

print(make_ruler(12))
print()
print(make_grid(4, 4))