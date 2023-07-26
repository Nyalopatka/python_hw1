n = int(input("введите длину шоколадки: "))
m = int(input("введите ширину шоколадки: "))
k = int(input("введите кол-во плиток которое нужно отломить: "))
if k<n*m and ((k % n == 0) or (k % m == 0)):
    print(f"{n} {m} {k} -> yes")
else:print(f"{n} {m} {k} -> no")
