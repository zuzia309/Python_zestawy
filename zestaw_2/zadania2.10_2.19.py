
def zad_10(line):
        return len(line.split())


def zad_11(word):
        return '_'.join(word)


def zad_12(line):
        words = line.split()
        first_letters = ''
        last_letters = ''

        for word in words:
            word = word.rstrip(",.")
            first_letters += word[0]
            last_letters += word[-1]

        return "Z pierwszych liter: ", first_letters, "  Z ostatnich liter: ", last_letters


def zad_13(line):
        words = line.split()
        sum = 0

        for word in words:
            only_letters = ''
            for char in word:
                    if char.isalpha():
                            only_letters += char
            sum += len(only_letters)

        return sum


def zad_14(text):

    words_raw = text.split()
    words_clean = []

    for word in words_raw:
        word = word.rstrip(".,")
        words_clean.append(word)

    max_len = max(len(word) for word in words_clean)
    longest = []

    for w in words_clean:
        if len(w) == max_len:
            longest.append(w)

    return longest, max_len



def zad_15(L):
        return ''.join(str(num) for num in L)


def zad_16(line):
        return line.replace("GvR", "Guido van Rossum")


def zad_17(line):
        words_before = line.split()
        words_after = []

        for word in words_before:
                word = word.rstrip(",.")
                word = word.lower()
                words_after.append(word)

        alphabetically_sorted = sorted(words_after)
        length_sorted = sorted(words_after, key=len)

        return alphabetically_sorted, length_sorted


def zad_18(number):
        return str(number).count('0')


def zad_19(L):
        word_L = ''
        for num in L:
            str_num = str(num).zfill(3)
            word_L += str_num

        return word_L



#---------------------- main -----------------------


line = ("Artificial intelligence and machine learning\n" "are transforming the world of technology.\n"
        "Python plays a key role in this revolution.")

word = "Zuzanna"
L = [1, 22, 50, 3, 7, 19, 43, 28, 111]
line_gvr = "GvR"
large_number = 12340456005544067


print("Zadanie 10: \n", zad_10(line))
print("\nZadanie 11: \n", zad_11(word))
print("\nZadanie 12: \n", zad_12(line))
print("\nZadanie 13: \n", zad_13(line))
print("\nZadanie 14: \n", zad_14(line))
print("\nZadanie 15: \n", zad_15(L))
print("\nZadanie 16: \n", zad_16(line_gvr))
print("\nZadanie 17: \n", zad_17(line))
print("\nZadanie 18: \n", zad_18(large_number))
print("\nZadanie 19: \n", zad_19(L))

