#Napisz algorytm sortowania danych za pomocą algorytmu sortowania bąbelkowego.

def bubblesort(t):
  n = len(t)
  for i in range(n-1):
    for j in range(n-1-i):
      if t[j] > t[j+1]:
        t[j], t[j+1] = t[j+1], t[j]
        
T = [4,2,7,1,3]
print("Przed sortowaniem", T)
bubblesort(T)
print("Po sortowaniu", T)

#Zaimplementuj algorytm sortowania przez wstawianie do posortowania listy liczb.

def insertionsort(u):
  o = len(u)
  for i in range(1,o):
    klucz = u[i]
    j = i-1
    while j >= 0 and u[j] > klucz:
      u[j+1] = u[j]
      j-=1
      u[j+1] = klucz

U = [4,2,7,1,3]
print("Przed sortowaniem", U)
insertionsort(U)
print("Po sortowaniu", U)

#Napisz algorytm sortowania szybkiego (quicksort) do sortowania danych.

def quicksort(v):
  if len(v) <= 1:
    return v
  else:
    pivot = v[0]
    less = [x for x in v[1:] if x <= pivot]
    greater = [x for x in v[1:] if x > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

V = [4,2,7,1,3]
print("Przed sortowaniem", V)
quicksort(V)
print("Po sortowaniu", quicksort(V))

#Zaimplementuj algorytm wyszukiwania binarnego dla posortowanej listy liczb.



#Napisz program, który znajdzie największy wspólny dzielnik dwóch liczb za pomocą algorytmu Euklidesa.

