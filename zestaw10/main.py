import tkinter as tk
from tkinter import messagebox
import random

RUCHY = ("Papier", "Kamień", "Nożyce")
WYGRANE = {"Papier": "Kamień", "Kamień": "Nożyce", "Nożyce": "Papier"}

def losuj():
    return random.choice(RUCHY)

def rozstrzygnij(gracz, pc):
    if gracz == pc:
        return "Remis!"
    if WYGRANE[gracz] == pc:
        return "Wygrałeś!"
    return "Przegrałeś!"

def zagraj(ruch_gracza):
    ruch_pc = losuj()
    wynik = rozstrzygnij(ruch_gracza, ruch_pc)

    messagebox.showinfo(
        "Wynik gry",
        f"Twój wybór: {ruch_gracza}\n"
        f"Wybor komputera: {ruch_pc}\n\n"
        f"{wynik}"
    )

root = tk.Tk()
root.title("PKN — Papier/Kamień/Nożyce")
root.geometry("600x250")

tk.Label(root, text="Papier – Kamień – Nożyce", font=("Arial", 18, "bold")).pack(pady=15)

btns = tk.Frame(root)
btns.pack(pady=10)

tk.Button(btns, text="Papier", width=14, font=("Arial", 13),
          command=lambda: zagraj("Papier")).grid(row=0, column=0, padx=10)
tk.Button(btns, text="Kamień", width=14, font=("Arial", 13),
          command=lambda: zagraj("Kamień")).grid(row=0, column=1, padx=10)
tk.Button(btns, text="Nożyce", width=14, font=("Arial", 13),
          command=lambda: zagraj("Nożyce")).grid(row=0, column=2, padx=10)

tk.Button(root, text="Zamknij", command=root.destroy).pack(pady=20)

root.mainloop()

#Na systemie macOS przy włączonym trybie ciemnym występowały problemy z wyświetlaniem tekstu w oknie aplikacji, dlatego wynik gry prezentowany jest w oknie dialogowym.
#Zastosowane rozwiązanie zapewnia poprawne działanie programu i spełnia wymagania zadania.