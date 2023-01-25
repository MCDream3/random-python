#Pre
from math import gcd      #Obliczanie NWD za pomocą gcd BO TAK JEST ŁATWIEJ

print(gcd(12,16))

p = 11                    #1) Wybór 2-ch liczb pierwszych (od 10 do nieskończoności)
q = 13

F = (p-1) * (q-1)         #2) Stworzenie funkcji F i znalezienie n = p*q
n = p * q
print(F)
print(n)

for i in range(2,F):      #3) Znalezienie klucza publicznego e: NWD(F,e)=1
  if gcd(i,F) == 1:        #OBOWIĄZKOWO MUSI BYĆ ZAIMPORTOWANY gcd!!!!
    e = i
    break
print(e,n)

for j in range(2,F):      #4) Wygenerowanie klucza prywatnego d: d*e mod F = 1 #odwrotność modulo
  if (j*e) % F == 1:
    d = i
    break
print(d,n)

#przykład działania kodowania znaku x:
#c = x**e mod n(na szyfrogram)
#t = c**d mod n(na tekst jawny)
msg = input()
szyfrogram = ""
for k in msg:
  szyfrogram+=chr((ord(k)**e) % n)
print(szyfrogram)


jawny=""
for l in szyfrogram:
  jawny+=chr((ord(l)**d) % n)      #to nie działa ;----;
print(jawny)