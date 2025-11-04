"""
L = [3, 5, 4] ; L = L.sort()
sort() zmienia listę bezpośrednio, więc nie trzeba jej przypisywać ponownie
"""
#poprawnie
L = [3, 5, 4]
L.sort()
print(L)

"""
x, y = 1, 2, 3
Nie da się przypisać trzech wartości do dwóch zmiennych naraz
"""
#poprawnie
x, y, z = 1, 2, 3
print(x, y, z)

"""
X = 1, 2, 3 ; X[1] = 4
Krotka jest niezmienialna – nie można edytować jej elementów
"""
#poprawnie
X = [1, 2, 3]
X[1] = 4
print(X[1])

"""
X = [1, 2, 3] ; X[3] = 4
Indeks 3 nie istnieje, bo elementy listy są numerowane od 0 do 2
"""
#poprawnie
Y = [1, 2, 3]
Y[2] = 4
print(Y[2])


"""
X = "abc" ; X.append("d")
append() działa tylko dla list, nie dla łańcuchów tekstowych
"""
#poprawnie
A = "abc"
A += "d"
print(A)

"""
L = list(map(pow, range(8)))
pow() potrzebuje dwóch argumentów, a tutaj przekazano tylko jeden
"""
#poprawnie
B = list(map(pow, range(8), [2] * 8))
print(B)
