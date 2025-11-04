"""
Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float) i wypisujący x oraz trzecią potęgę x.
Zatrzymanie programu następuje po wpisaniu z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby,
to program ma wypisać komunikat o błędzie i kontynuować pracę.
"""
while True:
    x = input("Podaj liczbe rzeczywista lub wpisz 'stop' aby zatrzymac program: ")
    if x.lower() == "stop":
        break
    try:
        num = float(x)
        print(f"Trzecia potega liczby {num} wynosi {num**3}")
    except:
        print("Blad, wprowadz liczbe")

