 #  1. Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literkę 
  
a = input()
print(f"{a[0]} i {a[-1]}" ) 
  
 # 2. Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej 
  
b = input() 
print(b[1:-1]) 
print(b[1 : len(b) - 1]) 
for i in range(1, len(b) - 1): 
  print(b, end=' ') 
          
 # 3. Wypisz 4 ostatnie literki z wpisanego napisy w kolejności od końca 
  
c = input() 
print(c[-1:-5:-1]) 
print(c[:-5:-1]) 
  
for i in range(len(c) - 1): 
  print(c, end=" ") 
  
C =list(c) 
C.reverse() 
c = "".join(C) 
print(c[:4]) 
  
 # 4. Waga napisu to suma kodów ascii jego liter. Zważ wpisny napis 
  
d = input() 
s = 0 
  
for i in d: 
  s += ord(i) 
print(s) 
  
 # 5. Policz ile we wpisanym napisie jest liter A. 
  
e = input() 
s = 0 

for i in e:
  if i == "a":
    s += 1
print(s)

#Zad6

