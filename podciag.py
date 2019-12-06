#Dane jest n ≥ 2 oraz ciąg liczb całkowitych a1, a2, ..., an. Podaj algorytm znajdowania długości najdłuższego podciągu kolejnych, takich samych liczb w tym ciągu.#

import random
def zad4(m,n):
    a = 1
    b = 0
    tab = []
    for i in range(n):
        tab.append(random.randint(2, m))
    for i in range(1, n):
        if tab[i] == tab[i - 1]:
            a += 1
        else:
            if a > b:
                b = a
                a = 1
    print("Najdłuższy podciąg zawiera", b, "liczb")
    print("Ciąg: ", tab)

m=int(input("Podaj liczbę naturalną M, która będzie najwyższą losową liczbą"))
n=int(input("Podaj liczbę naturalną N, która będzie długością ciągu"))
zad4(m,n)