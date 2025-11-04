"""
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;

Podany kod nie jest poprawny, ponieważ w pythonie nie kończymy lini średnikami.
"""
# poprawny kod
x = 2; y = 3
if (x > y):
    result = x
else:
    result = y


"""
for i in "axby": if ord(i) < 100: (print (i))

Nie jest poprawne, bo w Pythonie wymagane sa wcięcia, więc i if i print musi byc w nowej lini.
"""

#poprawny kod
for i in "axby":
    if ord(i) < 100:
        print (i)



"""
for i in "axby": print (ord(i) if ord(i) < 100 else i)

Jest ok.
"""

for i in "axby": print (ord(i) if ord(i) < 100 else i)
