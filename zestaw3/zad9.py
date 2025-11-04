"""
Mamy daną listę sekwencji (listy lub krotki) różnej długości zawierających liczby.
Znaleźć listę zawierającą sumy liczb z tych sekwencji. Przykładowa sekwencja [[],[4],(1,2),[3,4],(5,6,7)],
spodziewany wynik [0,4,3,7,18].
"""

sekwencja = [[],[4],(1,2),[3,4],(5,6,7)]
print(sekwencja)
print(f"Lista zawierająca sumy liczb sekwencji: {[sum(seq) for seq in sekwencja]}")
