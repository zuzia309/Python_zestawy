"""
Dla dwóch sekwencji liczb lub znaków znaleźć: (a) listę elementów występujących jednocześnie w obu sekwencjach (bez powtórzeń),
(b) listę wszystkich elementów z obu sekwencji (bez powtórzeń).
"""

L1 = [1, 2, 3, 4, 5, 6, 7]
L2 = [5, 2, 7, 2, 8, 8]

print(f"L1: {L1}")
print(f"L2: {L2}")
print(f"lista elementow wystepujacych jednoczesnie L1 i L2: {list(set(L1) & set(L2))}")
print(f"lista elementow występujących lacznie w L1 i L2: {list(set(L1) | set(L2))}")

print()
S1 = "transport"
S2 = "skuter"
print(f"S1: {S1}")
print(f"S2: {S2}")
print(f"lista liter występujacych jednoczesnie w S1 i S2: {list(set(S1) & set(S2))}")
print(f"lista liter występujacych lacznie w S1 i S2: {list(set(S1) | set(S2))}")