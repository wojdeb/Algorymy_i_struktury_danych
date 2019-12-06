"""
Podaj rekurencyjną funkcję SUMACYFR(n) znajdującą dla danej liczby naturalnej n sumę cyfr tej liczby
"""

def Zad2(n):
    if n > 0:
        return n%10 + Zad2(n//10)
    return 0

n = 0
while n<1:
    n = int(input("Podaj n: "))
print("Suma cyfr", n, "to: ", Zad2(n))