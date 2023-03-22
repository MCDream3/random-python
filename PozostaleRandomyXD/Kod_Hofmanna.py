#kod hofmanna is so hard    D:< 

W = "ABCCCDDDDDEFGGGHHIJJ"
E = "AB3C5DEF3G2HI2J" #<---to ma wyjść jeśli to wszystko działa
H=""                                                         #|
ilosc=1                                                      #|
                                                             #|
for i in range(1,len(W)-1):      #<---------------------------|
  if W[i] == W[i+1]:
    ilosc += 1
  else:
    if ilosc > 1:
      H += str(ilosc)
    H += W[i]
    ilosc = 1
if ilosc > 1:
  H += str(ilosc)
H += W[i]

print(W)
print(H)
