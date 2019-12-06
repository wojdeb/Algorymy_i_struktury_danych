"""
Dane jest n >= 2 oraz ciąg 2*n liczb całkowitych a1, a2, ..., a2*n. Podaj algorytm sortowania tego ciągu tak, aby liczby a1, a2, ..., an były posortowane nierosnąca, a liczby an+1, an+2, ..., a2*n były posortowane niemalejąca. Do sortowania obydwu podciągów użyj dwóch różnych metod sortowania. Nie jest dozwolone wykorzystywanie dodatkowych tablic.
"""

import random

def zad3(n, x, y):
    tab = []
    for i in range(2 * n):
        tab.append(random.randint(x, y + 1))
    print("Nieposortowany ciąg:")
    print(tab)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            if tab[j] > tab[j - 1]:
                tab[j], tab[j - 1] = tab[j - 1], tab[j]
    for j in range(n +1, (2 * n)):
        r = tab[j]
        i = j - 1
        while i > n - 1 and tab[i] > r:
            tab[i + 1] = tab[i]
            i -= 1
        tab[i + 1] = r
    print("\nPosortowany ciąg:")
    print(tab)

n=0
while n < 2:
    n = int(input("Podaj liczbę n:"))
    x = int(input("Podaj dolny zakres liczb:"))
    y = int(input("Podaj górny zakres liczb:"))

zad3(n, x, y)