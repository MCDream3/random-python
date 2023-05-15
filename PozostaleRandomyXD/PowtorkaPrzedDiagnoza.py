#WSTĘP

# 1. Oblicz sumę liczb 3-cyfrowych

suma = 0
for i in range(100,1000):
  suma = suma + i
print(suma)

# 2. Oblicz sumę i ilość dwucyfrowych wielokrotności liczby 6

suma = 0
ilosc = 0
for j in range(10,100):
  if j % 6 == 0:
    suma += j
    ilosc += 1
print(suma)
print(ilosc)


# 3. Znajdź największą liczbę wśród 5 wylosowanych przez program liczb 4-cyfrowych

import random

liczby = [random.randint(1000,10000) for k in range(5)]
najwieksza = liczby[0]

for liczba in liczby[1:]:
  if liczba > najwieksza:
    najwieksza = liczba
print(najwieksza)

# 4. Podaj sumę cyfr w dowolnej liczbie

lczb = input("Podaj liczbę:")
suma = 0

for cyfra in lczb:
  suma += int(cyfra)
print(suma)

# 5. Znajdź najmniejszą cyfrę we wpisanej przez usera liczbie 3-cyfrowej

lcz = input("Podaj liczbę trzycyfrową:")

najmniejsza_cyfra = int(lcz[0])

for cyfra in lcz:
  cyfra = int(cyfra)
  if cyfra < najmniejsza_cyfra:
    najmniejsza_cyfra = cyfra
print("Najmniejsza cyfra w podanej liczbie to:", najmniejsza_cyfra)  

# - ALGORYTMY

# 1. Sprawdź czy wpisana przez usera liczba jest pierwsza

licz = int(input("Podaj liczbę:"))
if licz < 2:
  print("Liczba ist nicht pierwsza!! XD")
else:
  for i in range(2, int(licz ** 0.5) + 1):
    if licz % 1 == 0:
      print("Liczba wciąż nie jest pierwsza!!")
      break
  else:
    print("Liczba ist pierwsza!!")

# 2. Sprawdź czy wpisana przez usera liczba jest złożona

import math

def Czy_Zlozona(liczba):
  if liczba < 2:
    return False
  if liczba == 2:
    return True
  if liczba % 2 == 0:
    return True
  granica = math.isqrt(liczba) + 1
  for dzielnik in range(3, granica, 2):
    if liczba % dzielnik == 0:
      return True
    return False

wpisana_liczba = int(input("Podaj liczbę:"))
if Czy_Zlozona(wpisana_liczba):
  print("BRAWO LICZBA JEST ZŁOŻONA!!")
else:
  print("spróbuj inną bo ta nie jest złożoną..")

# 3. Sprawdź czy wpisana przez usera liczba jest względnie pierwsza z 24

LICZBA = int(input("Podaj jakąś liczbę:"))

for DZIELNIK in range(2,25):
  if LICZBA % DZIELNIK == 0 and 24 % DZIELNIK == 0:
    print("Podana liczba nie jest względnie pierwsza z 24")
    return

print("Podana liczba jest względnie pierwsza z 24")

# 4. Zakoduj szyfrem CEZARA i kluczem k słowo s.



# 5. Dodaj dwa ułamki a/b + c/d. Zapisz sumę jako ułamek nieskracalny i liczbę mieszaną.

def nwd(a, b):
  while b:
    a, b = b, a % b
  return a

def dodaj_ulamki(a,b,c,d):
  wspolny_m = b * d // nwd(b, d)

  nowy_licznik_a - a * (wspolny_m // b)
  nowy_licznik_c - c * (wspolny_m // d)
  suma_l = nowy_licznik_a + nowy_licznik_c

  if suma_l % wspolny_m == 0:
    liczba_calkowita = suma_l // wspolny_m
    return liczba_calkowita, None
  else:
    nwd_suma = nwd(suma_l, wspolny_m)
    skracalny_licznik = suma_licznikow // nwd_suma
    skracalny_mianownik = wspolny_m // nwd_suma
    return skracalny_licznik, skracalny_mianownik

a = int(input("Podaj wartosc a:"))
b = int(input("Podaj wartosc b:"))
c = int(input("Podaj wartosc c:"))
d = int(input("Podaj wartosc d:"))

# 6. Znajdź NWW dwóch wpisanych przez usera liczb

print("EZ")

def NWD(a, b):
  while b:
    a, b = b, a % b
    return a

def NWW(a, b):
  NWD_ab = NWD(a, b)
  return (a * b) // NWD_ab

liczba1 = int(input("Podaj liczbę nr1:"))
liczba2 = int(input("Podaj liczbę nr2:"))

wynik = NWW(liczba1, liczba2)
print("NWW:", wynik)


# - KARTKA

# 1. Oblicz wartość ONP - 8822+/234*---



# 2. Znajdź postać ONP dla pisanego wyrażenia - (3+8)/4-6*(3*4/2)



# 3. Napisz na kartce algorytm NWD (obie wersje) i przeprowadz symulacje kroków dla podanych liczb - dowolny i a=35 b=56




# - NAPISY

# 1. Znajdź ilość liter C we wpisanym napisie



# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp



# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.


