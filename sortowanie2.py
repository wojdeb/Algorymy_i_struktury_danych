"""
Dane jest n >= 1 oraz kwadratowa tablica A liczb całkowitych, mająca n wierszy i n kolumn. Podaj algorytm sortowania wierszy tej tablicy tak, aby sumy elementów w kolejnych wierszach (od pierwszego do n-tego) tworzyły ciąg niemalejący. Dozwolone jest wykorzystanie dodatkowej, jednowymiarowej tablicy
"""

import random

def zad5(n, x, y):
    A = [[None] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            A[i][j] = random.randint(x, y)
    s = []

    for i in range(n):
        suma = 0
        for j in range(n):
            suma += A[i][j]
        s.append(suma)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if s[j] < s[j - 1]:
                s[j], s[j - 1] = s[j - 1], s[j]
                A[j], A[j - 1] = A[j - 1], A[j]
    print()
    for i in range(n):
        print(A[i], end="")
        suma = 0
        for j in range(n):
            suma += A[i][j]
        print("   suma: ", suma)

n = 0
while n<1:
    n = int(input("Podaj n (długość wierszy i kolumn): "))
    x = int(input("Podaj dolny zakres liczb: "))
    y = int(input("Podaj górny zakres liczb: "))

zad5(n, x, y)