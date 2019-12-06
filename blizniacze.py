# Dane są dwie liczby naturalne m oraz n. Podaj algorytm, który sprawdzi, czy liczby te są bliźniacze.#

def zad1(m,n):
    if first(m) and first(n):
        if m+2==n or m-2==n:
            print(m, "i ", n, "to liczby bliźniacze")
        else:
            print(m, "i ", n, "nie są liczbami bliźniaczymi")
    else:
        print(m, "i ", n, "nie są liczbami bliźniaczymi")
def first(m):
    x = 2
    if m < x:
        print(m, "nie jest liczbą pierwszą")
        return False
    while True:
        if x == m:
            print(m, "jest liczbą pierwszą")
            return True
        if m % x == 0:
            print(m, "nie jest liczbą pierwszą")
            return False
        x=x+1
m=int(input("Podaj liczbę naturalną M: "))
n=int(input("Podaj liczbę naturalną N: "))
zad1(m,n)
