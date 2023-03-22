n = int(input())
L = list(map(int,input().split()))
L.insert(0,0)

for i in range(n):
   print(L[i+1]-L[i], end=" ")
