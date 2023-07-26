import random
monetki = int(input("введите кол-во 'coins': "))
orel = 0
reshka = 0
for i in range(monetki+1):
    if random.randint(0,1) == 0:
        orel += 1
    else: reshka += 1
if orel >= reshka:
    print(f"нужно перевернуть {reshka} 'coins'")
else:print(f"нужно перевернуть {orel} 'монет'")