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

# 8 8 2 2 + / 2 3 4 * - - -
# 8 8 4 / 2 3 4 * - - -
# 8 2 2 3 4 * - - -
# 8 2 2 12 - - -
# 8 2 -14 - -
# 8 -16 -
# -24

# 2. Znajdź postać ONP dla pisanego wyrażenia - (3+8)/4-6*(3*4/2)

# Postać ONP dla tego wyrażenia to -    3 8 + 4 / 6 3 4 * 2 / * -

# 3. Napisz na kartce algorytm NWD (obie wersje) i przeprowadz symulacje kroków dla podanych liczb - dowolny i a=35 b=56

def nwd_odejmowanie(a, b):
  while a != b:
    if a > b:
      a = a - b
    else:
      b = b - a
  return a

def nwd_modulo(a, b):
  while b != 0:
    a, b = b, a % b
  return a

def symulacja_krokow(a, b):
  print(f"Symulacja kroków dla a = {a} i b = {b}:")
  print("Metoda odejmowania")
  krok = 1
  while a!= b:
    if a > b:
      a = a - b
    else:
      b = b - a
    print(f"Krok{krok}: a = {a}, b = {b}")
    krok += 1

  print("Metoda modulo:")
  krok = 1
  while b != 0:
    a,  b = b, a % b
    print(f"Krok{krok}: a = {a}, b = {b}")
    krok += 1

a = 35
b = 56

wynik_odejmowanie = nwd_odejmowanie(a, b)
wynik_modulo = nwd_modulo(a, b)
print(f"NWD za pomocą metody odejmowania dla a = {a} i b = {b}: {wynik_odejmowanie}")
print(f"NWD za pomocą metody modulo dla a = {a} i b = {b}: {wynik_modulo}")

symulacja_krokow(a, b)


# - NAPISY

# 1. Znajdź ilość liter C we wpisanym napisie

napis = input()
ilosc_c = napis.count("C")
print("Ilość liter c w napisie wynosi:", ilosc_c)

# 2. Sprawdź czy literki w napisie są w porządku nierosnącym: np ZOO, WOK, WODA itp

nap = input()
for i in range(len(nap)-1):
  if ord(nap[i]) < ord(nap[i+1]):
    print("UWAGA!!! LITERY NIE SĄ W PORZĄDKU NIE ROSNĄCYM!!")
    break
  else:
    print("Litery są w porzą w porządku nie rosnącym")

# 3. Podaj najdłuższy z 3 wpisanych przez usera wyrazów.

w1 = input("Podaj pierwszy wyraz ciulu:")
w2 = input("Dobra teraz drugi:")
w3 = input("Został ostatni:")
najdluzszy_wyraz = ""

if len(w1) > len(najdluzszy_wyraz):
  najdluzszy_wyraz = w1
if len(w2) > len(najdluzszy_wyraz):
  najdluzszy_wyraz = w2
if len(w3) > len(najdluzszy_wyraz):
  najdluzszy_wyraz = w3

print(f"Idk jak tego nie zauważyłeś ale nadłuższy wyraz to:{najdluzszy_wyraz}")
