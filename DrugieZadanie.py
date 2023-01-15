n = int(input())

L = list(map(int, input().split()))

ilosc = 0

for i in range(n):

  if L[i] < 7: ilosc += 1

print(ilosc)