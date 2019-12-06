#Dane jest n ≥ 2 oraz ciąg liczb całkowitych a1, a2, ..., an, wszystkich różnych między sobą. Podaj algorytm znajdowania drugiej co do wartości liczby w tym ciągu.#

import random

m=int(input("Podaj liczbę naturalną M, która będzie wartością maksymalną ciągu"))
n=int(input("Podaj liczbę naturalną N, która będzie długością ciągu"))
def zad3(m,n):
    tab = []
    for i in range(n):
        tab.append(random.randint(2, m))
    max1 = 0
    max2 = 0
    for i in range(n):
        if tab[i] > max1:
            max1 = tab[i]
    for i in range(n):
        if tab[i] != max1:
            if tab[i] > max2:
                max2 = tab[i]
    if max1 == max2:
        print("Wszystkie liczby są równe")
    elif max2 < max1:
        print("Drugą co do wartości liczbą w tym ciągu jest", max2)
    print("ciąg: ", tab)

zad3(m,n)