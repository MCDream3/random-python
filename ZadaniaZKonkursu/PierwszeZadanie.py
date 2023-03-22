A, B = map(int,input().split())

if (A + B) != 100: print("SKANDAL")

elif A > B: print("Bitek")

elif B > A: print("Bajtek")

else: print("Remis")
